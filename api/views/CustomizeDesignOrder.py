# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import OrderList
from ..serializers import CustomizeDesignOrderListSerializer  # Assuming you have a serializer for OrderList model
from django.http import JsonResponse

class CustomizeDesignOrderView(APIView):
    def post(self, request):
        serializer = CustomizeDesignOrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Customize Design Order data inserted successfully', 'status': 201, 'success': True, 'data': serializer.data}, status=201)
        return JsonResponse({'message': 'Customize Design Order data insertion failed', 'status': 400, 'success': False, 'errors': serializer.errors}, status=400)
