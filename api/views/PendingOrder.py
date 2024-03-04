from django.shortcuts import render
from rest_framework.views import APIView
from backend.models import OrderList, AccountDetails
from django.http import JsonResponse

class PendingOrderview(APIView):
    def post(self, request):
        # Get the first name from the request data
        first_name = request.data.get('first_name')

        # Check if an account exists with the given first name
        if first_name:
            account = AccountDetails.objects.filter(first_name=first_name).exists()
            if not account:
                return JsonResponse({'message': 'Account not found with the provided first name', 'status': 404, 'success': False}, status=404)

        # Fetch orders with the provided name and status "1"
        pending_orders = OrderList.objects.filter(customername=first_name, status='1').values()
        
        # Convert queryset to list for JSON serialization
        pending_orders_list = list(pending_orders)
        
        # Return JSON response
        # return JsonResponse(pending_orders_list, safe=False)
        return JsonResponse({'message': 'Pending Order data retreived successfully', 'status': 200, 'success': True, 'data': pending_orders_list}, status=200)
