from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsViews, name="collectionsViews"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productViews, name="productViews"),
]
