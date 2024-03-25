# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import OrderList
from ..serializers import CustomizeThemeDesignKidsOrderListSerializer  # Assuming you have a serializer for OrderList model
from django.http import JsonResponse

class CustomizeThemeDesignKidOrderView(APIView):
    def post(self, request):
        serializer = CustomizeThemeDesignKidsOrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Customize Theme Design Order data inserted successfully', 'status': 201, 'success': True, 'data': serializer.data}, status=201)
        return JsonResponse({'message': 'Customize Theme Design Order data insertion failed', 'status': 400, 'success': False, 'errors': serializer.errors}, status=400)
