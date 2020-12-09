from django.urls import path
from app.view.product_image_view import view

urlpatterns = [
    path("product_image/", view.product_images),
    path("product_details/<int:image_id>/", view.product_image_details)
]
