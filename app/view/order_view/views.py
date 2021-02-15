from django.views.decorators.csrf import csrf_exempt
from app.Dto.OrderDto import *
from app.serializer import OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app.service_provider import app_service_provider


@api_view(['POST', 'GET'])
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        orders = app_service_provider.order_management_service().list_order()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        pass


def __set_attribute_from_request(create_order_dto, request):
    create_order_dto.product_name = request.data.get('product_name', False)
    create_order_dto.shipping_address = request.data.get('shipping_address', False)
    create_order_dto.unit_price = request.data.get('unit_price', False)
    create_order_dto.quantity = request.data.get('quantity', False)
    create_order_dto.customer_last_name = request.data.get('last_name', False)


def __get_attribute_from_request(request):
    create_order_dto = CreateOrderDto()
    create_order_dto.customer_last_name = request.data.get('customer_last_name')
    __set_attribute_from_request(create_order_dto, request)
    return create_order_dto
