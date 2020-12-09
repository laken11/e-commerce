from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from app.serializer import ProductImageSerializer
from app.service_provider import app_service_provider
from rest_framework import status
from rest_framework.decorators import api_view
from app.Dto.ProductImageDto import ImageUrlDetails, RegisterImageUrl, ListImageUrl, EditImageUrl


@csrf_exempt
@api_view(['GET', 'POST'])
def product_images(request):
    if request.method == 'GET':
        images = app_service_provider.product_image_management_service().list_image()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        image = __set_attribute_from_request(request)
        serializer = app_service_provider.product_image_management_service().register_image(image)
        if serializer is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def product_image_details(request, image_id: int):
    if request.method == 'GET':
        image = app_service_provider.product_image_management_service().image_details(image_id)
        serializer = ProductImageSerializer(image, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        image = __set_attribute_from_request_edit(image_id, request)
        serializer = app_service_provider.product_image_management_service().edit_image(image_id, image)
        if serializer is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        app_service_provider.product_image_management_service().delete(image_id)
        return Response(status=status.HTTP_200_OK)


def __get_attribute_from_request(create_image_dto, request):
    create_image_dto.name = request.data['name']
    create_image_dto.file = request.data['file']


def __set_attribute_from_request(request):
    create_image_dto = RegisterImageUrl()
    create_image_dto.name = request.data['name']
    __get_attribute_from_request(create_image_dto, request)
    return create_image_dto


def __get_attribute_from_request_edit(edit_product_image_dto, request):
    edit_product_image_dto.name = request.data['name']
    edit_product_image_dto.file = request.data['file']


def __set_attribute_from_request_edit(image_id, request):
    edit_product_image_dto = EditImageUrl()
    edit_product_image_dto.id = image_id
    __get_attribute_from_request_edit(edit_product_image_dto, request)
    return edit_product_image_dto
