from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from projects.models import Projects
from django.views.generic import ListView, DetailView, TemplateView

from .forms import ProductForm, LoginUserForm, AdminRegistrationForm, KlientRegistrationForm

from .models import User, Manager, Klient, Product
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'products'
    # paginate_by = 5  # Количество товаров на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart')
        if not cart:
            cart = self.request.session['cart'] = {}
        context['cart'] = cart
        context['latest_projects'] = Projects.objects.order_by('-created_at')[:3]
        return context

    def get_queryset(self):
        return Product.objects.order_by('name')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'
    context_object_name = 'product'


class AddProductView(TemplateView):
    template_name = 'app/add_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['product_form'] = ProductForm()
        return context

    def post(self, request):
        if self.request.POST.get('form-type') == 'product_form':
            form_for_product = ProductForm(request.POST)
            if form_for_product.is_valid():
                product_form = form_for_product.save(commit=False)

                product_form.save()

                return redirect('app:add_product')

            return render(request, 'app/add_product.html', context={'product_form': form_for_product})


def about(request):
    return render(request, 'app/about.html')


def register_klient(request):
    if request.method == 'POST':
        form = KlientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('app:product_list')
    else:
        form = KlientRegistrationForm()
    return render(request, 'app/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('app:product_list')


def logout_user(request):
    logout(request)
    return redirect('app:login')


def register_user_by_admin(request):
    if request.method == 'POST':
        print(request.POST)
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:register_user_by_admin')
    else:
        form = AdminRegistrationForm()

    return render(request, 'app/register_user_by_admin.html', {'form': form})


from django.views.generic import ListView, DeleteView
from .models import OrderItem


class OrderListView(ListView):
    model = OrderItem
    template_name = 'app/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created']


def order_delete(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('app:order_list')

    return render(request, 'app/order_list.html', {'order': order})


def user_list(request):
    klients = Klient.klients.all()
    managers = Manager.managers.all()
    users = {
        'klients': klients,
        'managers': managers,
    }
    return render(request, 'app/user_list.html', users)


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('app:user_list')
