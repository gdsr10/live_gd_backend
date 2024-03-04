from django.shortcuts import render
from rest_framework.views import APIView
from backend.models import OrderList
from django.http import JsonResponse

class CancelViewOrderview(APIView):
    def post(self, request):
        # Get the first name from the request data
        first_name = request.data.get('first_name')

        # Check if first name is provided
        if not first_name:
            return JsonResponse({'message': 'First name is required', 'status': 400, 'success': False}, status=400)

        # Check if the first name exists in OrderList
        order_exists = OrderList.objects.filter(customername=first_name).exists()
        if not order_exists:
            return JsonResponse({'message': 'No orders found with the provided first name', 'status': 404, 'success': False}, status=404)

        # Fetch all orders with status "1"
        pending_orders = OrderList.objects.filter(customername=first_name, status='2').values()
        
        # Convert queryset to list for JSON serialization
        pending_orders_list = list(pending_orders)
        
        # Return JSON response
        # return JsonResponse(pending_orders_list, safe=False)
        return JsonResponse({'message': 'Cancel Order data retreived successfully', 'status': 200, 'success': True, 'data': pending_orders_list}, status=200)
