# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import AccountDetails
from ..serializers import AccountDetailsSerializer
from django.http import JsonResponse

class RegisterView(APIView):
    def post(self, request):
        serializer = AccountDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'Message': 'User Data inserterd successfully', 'Status':201, 'Success': 'True', 'data':[serializer.data]}, status=201)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'Message': 'User Data inserterd Failure', 'Status':400, 'Success': 'False', 'data':[serializer.errors]}, status=400)
