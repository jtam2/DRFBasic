from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
class BasicAPI(APIView):

    def get(self, request):
        data = {
            'first_name': 'grant',
            'last_name': 'zhu'
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        req_data = request.data
        data = {
            'first_name': 'HELLO',
            'last_name': 'HERE I AM'
        }
        time.sleep(900)
        return Response(data, status=status.HTTP_200_OK)