# views.py
from rest_framework.views import APIView
from django.http import JsonResponse
from backend.models import AccountDetails

class ResetPasswordView(APIView):
    def post(self, request):
        user_id = request.data.get('id')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return JsonResponse({'Message': 'Passwords do not match.', 'Status': 400, 'Success': 'False'}, status=400)

        print(user_id)
        print(password)
        print(confirm_password)

        try:
            user = AccountDetails.objects.get(id=user_id)
            # print(user)
            user.password = password
            user.confirm_password = confirm_password
            user.save()
            return JsonResponse({'Message': 'Password updated successfully', 'Status': 200, 'Success': 'True'}, status=200)
        except AccountDetails.DoesNotExist:
            return JsonResponse({'Message': 'User not found.', 'Status': 404, 'Success': 'False'}, status=404)
