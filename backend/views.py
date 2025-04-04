from django.views import View, generic
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import login, user_logged_in
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import ProductForm, RegistrationForm, OrderForm
from .models import *


class AllProductsView(View):
    def get_product(self,request):
        ask = request.GET
        products = Product.objects.all()
        if ask.get('search'):
            products = products.filter(
                Q(name__icontains=ask['search']) | Q(description__icontains=ask['search'])
            )
        response = [
            {
                'name': product.name,
                'description': product.description,
                'price': product.price
            } for product in products
        ]
        return JsonResponse(data={'response':response})


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    queryset = Product.objects.all()
    template_name = 'product_list.html'


def product_template(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, template_name='product.html', context={'product': product})


class ProductDetailView(generic.DetailView):
    model = Product

    def product_detail_view(request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            raise Exception('Product not exist')

        return render(
            request,
            'product_detailed.html',
            context={'product': product }
        )


class CategoryProductView(View):
    def get(self, category_id):
        products = Product.objects.filter(category_id=category_id).all()
        response = [
            {
                'name': product.name,
                'description': product.description,
                'price': product.price
            } for product in products
        ]
        return JsonResponse(data={'response': response})


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'categories.html'

    def get_queryset(self):
        return Category.objects.filter().all()

    def category_detail_view(request, pk):
        try:
            category_id = Category.objects.get(pk=pk)
        except:
            raise Exception('Product not exist')

        return render(
            request,
            'categories.html',
            context={'category': category_id}
        )


class CategoryTemplateView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='home')
    else:
        form = RegistrationForm()
    return render(request, template_name= 'register.html',context= {'form':form})


@login_required
def profile(request):
    return render(request, template_name= 'profile.html', context= {'user':request.user})


class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('profile')


def add_basket(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='profile')
        else:
            raise Exception('Form is not valid')
    else:
        form = OrderForm()
    return render(request, template_name= 'add_basket.html', context= {'form':form})


def edit_basket(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        for order in Order.objects.all():
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
            return redirect(to='profile', pk=pk)
    else:
        form = OrderForm()
    return render(request, template_name='edit_basket.html', context={'form':form})









