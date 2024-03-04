# serializers.py
from rest_framework import serializers
from backend.models import AccountDetails, ItemList, OrderList

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['id', 'first_name', 'last_name', 'mobile_number', 'dob', 'email', 'password', 'confirm_password', 'is_admin', 'otp', 'otp_created_at']


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class AccountPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['password', 'confirm_password']


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = '__all__'


class OnlineOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'customername', 'title', 'price', 'image_url', 'order_type_name', 'order_type', 'status']



class CustomizeDesignOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'customername', 'order_type_name', 'order_type', 'material_name', 'size', 'bust', 'waist', 'hips', 'status']



class CustomizeThemeDesignOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'customername', 'order_type_name', 'order_type', 'material_name', 'size', 'bust', 'waist', 'hips', 'status']