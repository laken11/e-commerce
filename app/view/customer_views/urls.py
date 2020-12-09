from django.urls import path
from app.view.customer_views import views

urlpatterns = [
    path('customers/', views.customer_list, name='customers'),
    path('customerdetails/<int:customer_id>/', views.customer_details, name='customer_details'),
]
