from django.views.decorators.csrf import csrf_exempt
from app.Dto.CategoryDto import RegisterCategoryDto
from app.serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.service_provider import app_service_provider


@csrf_exempt
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categorys = app_service_provider.category_management_service().list_category()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        category = __set_attribute_from_request(request)
        serializer = app_service_provider.category_management_service().register_category(category)
        if serializer is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT'])
def category_details(request, category_id: int):
    if request.method == 'GET':
        category = app_service_provider.category_management_service().category_details(category_id)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        category = __set_attribute_from_request(request)
        serializer = app_service_provider.category_management_service().edit_category(category_id, category)
        if serializer is True:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_super_category(request):
    if request.method == 'GET':
        categorys = app_service_provider.category_management_service().get_super_category()
        if categorys is []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sub_category(request, parent_id: int):
    if request.method == 'GET':
        category = app_service_provider.category_management_service().get_sub_category(parent_id)
        if category is []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def __get_attribute_from_request(create_category_dto, request):
    create_category_dto.name = request.data.get('name', False)
    create_category_dto.parent = request.data.get('parent', False)


def __set_attribute_from_request(request):
    create_category_dto = RegisterCategoryDto()
    create_category_dto.name = request.data.get('name', False)
    __get_attribute_from_request(create_category_dto, request)
    return create_category_dto
