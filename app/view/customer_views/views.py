from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from app.serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Customer
from rest_framework import status
from app.service_provider import app_service_provider
from app.Dto.CustomerDto import RegisterCustomerDto, EditCustomerDto


@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = app_service_provider.customer_management_service().list_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        customer = __set_attribute_from_request(request)
        password = customer.password
        confirm_password = customer.confirm_password
        if password == confirm_password:
            serializer = app_service_provider.customer_management_service().register_customer(customer)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, customer_id: int):

    if request.method == 'GET':
        customer = app_service_provider.customer_management_service().customer_details(customer_id)
        serializer = CustomerSerializer(customer, many=False)
        if serializer is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    elif request.method == 'PUT':
        customer = __set_attribute_from_request_for_edit(customer_id, request)
        serializer = app_service_provider.customer_management_service().edit_customer(customer, customer_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        app_service_provider.customer_management_service().delete_customer(customer_id)
        return HttpResponse(status=204)


def __get_attribute_from_request(create_customers_dto, request):
    create_customers_dto.state = request.POST.get('state', False)
    create_customers_dto.country = request.POST.get('country', False)
    create_customers_dto.phone = request.POST.get('phone', False)
    create_customers_dto.address = request.POST.get('address', False)
    create_customers_dto.first_name = request.POST.get('first_name', False)
    create_customers_dto.last_name = request.POST.get('last_name', False)
    create_customers_dto.username = request.POST.get('username', False)
    create_customers_dto.email = request.POST.get('email', False)
    create_customers_dto.password = request.POST.get('password', False)
    create_customers_dto.confirm_password = request.POST.get('confirm_password', False)


def __set_attribute_from_request(request) -> RegisterCustomerDto:
    create_customers_dto = RegisterCustomerDto()
    create_customers_dto.state = request.data.get('state', False)
    __get_attribute_from_request(create_customers_dto, request)
    return create_customers_dto


def __get_attribute_from_request_for_edit(edit_customer_dto, request):
    edit_customer_dto.state = request.data['state']
    edit_customer_dto.country = request.data['country']
    edit_customer_dto.phone = request.data['phone']
    edit_customer_dto.address = request.data['address']
    edit_customer_dto.first_name = request.data['first_name']
    edit_customer_dto.last_name = request.data['last_name']
    edit_customer_dto.username = request.data['username']
    edit_customer_dto.email = request.data['email']


def __set_attribute_from_request_for_edit(customer_id: int, request):
    edit_customer_dto = EditCustomerDto()
    edit_customer_dto.id = customer_id
    __get_attribute_from_request_for_edit(edit_customer_dto, request)
    return edit_customer_dto


def __get_customer_or_raise_404(request, customer_id: int):
    try:
        customer = app_service_provider.customer_management_service().customer_details(customer_id)
        return customer
    except Customer.DoesNotExist as e:
        message = 'customer dose not exit'
        print(message)
        return e








