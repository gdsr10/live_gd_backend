from django.shortcuts import render
from rest_framework.views import APIView
from backend.models import OrderList
from django.http import JsonResponse

class AdCancelViewOrderview(APIView):
    def post(self, request):
        
        # Fetch all orders with status "1"
        pending_orders = OrderList.objects.filter(status='2').values()
        
        # Convert queryset to list for JSON serialization
        pending_orders_list = list(pending_orders)
        
        # Return JSON response
        # return JsonResponse(pending_orders_list, safe=False)
        return JsonResponse({'message': 'Cancel Order data retreived successfully', 'status': 200, 'success': True, 'data': pending_orders_list}, status=200)
