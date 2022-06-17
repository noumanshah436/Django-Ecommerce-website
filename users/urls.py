from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name="register"),
    # path('login', views.LoginPage, name="login"),
    # path('logout', views.LogoutPage, name="logout")
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),


    path('add-to-cart/', views.addToCart, name='addToCart'),
    path('cart/', views.viewCart, name='cart'),
    path('update-cart/', views.updateCart, name='updatecart'),
    path('delete-cart-item/', views.deleteCart, name='deleteCart'),


]
