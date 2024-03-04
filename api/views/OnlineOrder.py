# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import OrderList
from ..serializers import OnlineOrderListSerializer  # Assuming you have a serializer for OrderList model
from django.http import JsonResponse

class OnlineOrderView(APIView):
    def post(self, request):
        serializer = OnlineOrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Online Order data inserted successfully', 'status': 201, 'success': True, 'data': serializer.data}, status=201)
        return JsonResponse({'message': 'Online Order data insertion failed', 'status': 400, 'success': False, 'errors': serializer.errors}, status=400)
