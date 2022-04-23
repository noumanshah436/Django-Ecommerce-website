from django.urls import path
from . import views

# from store.controller import authview

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsViews, name="collectionsViews"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productViews, name="productViews"),
    path('addProduct', views.addProduct, name="addProduct"),
    path('delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('update/<int:id>/', views.updateProduct, name='updateProduct'),

    # path('register', authview.register, name="register"),
    # path('login', authview.LoginPage, name="login"),
    # path('logout', authview.LogoutPage, name="logout")
]
