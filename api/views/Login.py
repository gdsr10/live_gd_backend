# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import AccountDetails
from ..serializers import AccountDetailsSerializer
from django.http import JsonResponse

class LoginView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = AccountDetails.objects.get(email=email)
        except AccountDetails.DoesNotExist:
            # return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({'Message': 'User not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)

        if user.password == password:
            serializer = AccountDetailsSerializer(user)
            # return Response(serializer.data)
            return JsonResponse({'Message': 'User Data', 'Status':200, 'Success': 'True', 'data':[serializer.data]}, status=200)
        else:
            # return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data':[]}, status=401)
