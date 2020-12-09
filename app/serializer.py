from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=None, write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    phone = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=150)

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        return customer

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.user_id = validated_data.get('user_id', instance.user)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class StaffSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=50)
    user = serializers.StringRelatedField(read_only=True)
    job_title = serializers.CharField()

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()
        return instance


class ProductImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    file = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    def create(self, validated_data):
        return ProductImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=500)
    product_image = ProductImageSerializer(many=False, read_only=True)
    ProductImage_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True, many=False)
    category_name = serializers.CharField(read_only=True, max_length=500)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.ProductImage_id = validated_data.get('ProductImage_id', instance.ProductImage_id)
        instance.category = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance


class FeedbackSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(decimal_places=2, max_digits=50)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    payment_reference = serializers.CharField(max_length=10)
    approved = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class OrderSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(write_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    status = serializers.CharField(max_length=10)
    order_reference = serializers.UUIDField(default=uuid.uuid4())
    paid = serializers.BooleanField(default=False)
    shipping_address = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class OrderDetailsSerializer(serializers.Serializer):
    quality = serializers.IntegerField()
    unit_price = serializers.FloatField()
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def create(self, validated_data):
        return OrderDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass









