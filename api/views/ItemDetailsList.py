from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import ItemList
from ..serializers import ItemListSerializer
from django.http import JsonResponse

class ItemDetailsListView(APIView):
    
    def post(self, request):
        id = request.data.get('id')

        try:
            user = ItemList.objects.get(id=id)
            serializer = ItemListSerializer(user)
            # return Response(serializer.data)
            return JsonResponse({'Message': 'Item Data', 'Status':200, 'Success': 'True', 'data':[serializer.data]}, status=200)
        except ItemList.DoesNotExist:
            # return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({'Message': 'Item not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
