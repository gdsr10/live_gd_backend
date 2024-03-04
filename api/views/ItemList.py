from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import ItemList  # Import the ItemList model
from ..serializers import ItemListSerializer  # Import the serializer for the ItemList model
from django.http import JsonResponse

class ItemListView(APIView):
    
    def post(self, request):
        # Retrieve all items from the database
        items = ItemList.objects.all()
        # Serialize the items
        serializer = ItemListSerializer(items, many=True)
        # Return the serialized data as a JSON response
        return JsonResponse({'Message': 'Item List', 'Status':200, 'Success': 'True', 'data':serializer.data}, status=200)
