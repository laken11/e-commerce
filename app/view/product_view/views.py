from django.views.decorators.csrf import csrf_exempt
from app.Dto.ProductDto import CreateProductDto
from app.serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.service_provider import app_service_provider


@csrf_exempt
@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = app_service_provider.product_management_service().list_product()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        product = __set_attribute_from_request(request)
        product = app_service_provider.product_management_service().create_product(product)
        if product is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, product_id: int):
    if request.method == 'GET':
        product = app_service_provider.product_management_service().product_details(product_id)
        if product is False:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        product = __set_attribute_from_request(request)
        serializer = app_service_provider.product_management_service().edit_product(product_id, product)
        if serializer is False:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        product = app_service_provider.product_management_service().delete_product(product_id)
        if product is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def __get_attribute_from_request(product_dto, request):
    product_dto.name = request.data.get('name', False)
    product_dto.price = request.data.get('price', False)
    product_dto.description = request.data.get('description', False)
    product_dto.image_name = request.data.get('image_name', False)
    product_dto.category_name = request.data.get('category_name', False)


def __set_attribute_from_request(request):
    product_dto = CreateProductDto()
    product_dto.name = request.data.get('name', False)
    __get_attribute_from_request(product_dto, request)
    return product_dto
