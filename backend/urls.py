from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import product_template, ProductListView, CategoryTemplateView

urlpatterns = [
    path('',views.HomeTemplateView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name ='product_list'),
    path('product/<int:pk>/', product_template, name='product'),
    path('categories', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryTemplateView.as_view(), name='category'),
    path('contact/',views.ContactTemplateView.as_view(), name='contact'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('register/', views.register, name='register'),
    path('add_basket/', views.add_basket, name='add_basket'),
    path('edit_basket/<int:pk>/', views.edit_basket, name='edit_basket'),

]