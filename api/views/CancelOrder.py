from django.shortcuts import render
from rest_framework.views import APIView
from backend.models import OrderList
from django.http import JsonResponse

class CancelOrderview(APIView):
    def post(self, request):
        order_id = request.data.get('id')  # Get the ID of the order from the request data
        try:
            # Fetch the order by its ID
            order = OrderList.objects.get(id=order_id)
            # Update the status of the order to "confirmed" (Assuming status field is a CharField)
            order.status = '2'
            order.save()  # Save the changes to the database
            return JsonResponse({'message': 'Order cancelled successfully', 'status': 200, 'success': True})
        except OrderList.DoesNotExist:
            return JsonResponse({'message': 'Order not found', 'status': 404, 'success': False})
        except Exception as e:
            return JsonResponse({'message': str(e), 'status': 500, 'success': False})