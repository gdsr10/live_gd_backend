# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from backend.models import AccountDetails
from ..serializers import ForgotPasswordSerializer
import random
from django.http import JsonResponse
from twilio.rest import Client

class ForgotPasswordView(APIView):

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = AccountDetails.objects.get(email=email)
            except AccountDetails.DoesNotExist:
                # return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
                return JsonResponse({'Message': 'User with this email does not exist.', 'Status':404, 'Success': 'False'}, status=404)
            
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            user.otp = otp
            user.save()

            # # Send OTP to user's email
            # send_mail(
            #     'Password Reset OTP',
            #     f'Your OTP is: {otp}',
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False,
            # )

            # return Response({'success': 'OTP sent to your email address.'}, status=status.HTTP_200_OK)
            return JsonResponse({'Message': 'OTP sent to your email address.', 'Status':200, 'Success': 'True', 'id': user.id}, status=200)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'Message': 'OTP sent Failure', 'Status':400, 'Success': 'False', 'data':[serializer.errors]}, status=400)

