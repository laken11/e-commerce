from django.urls import path
from app.view.product_view import views

urlpatterns = [
    path('products/', views.products_list),
    path('product_details/<int:product_id>/', views.product_details)
]