from django.urls import path
from app.view.category_view import views

urlpatterns = [
    path('categorys/', views.category_list),
    path('categorydetails/<int:category_id>/', views.category_details),
    path('supercategory/', views.get_super_category),
    path('sub_category/<int:parent_id>/', views.get_sub_category)
]
