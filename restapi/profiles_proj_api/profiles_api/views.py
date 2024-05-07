from rest_framework.views import APIView
from rest_framework.response import Response


class BaseAPIView(APIView):

    def get(self,request,format=None):
        apiview=[
            'HTTP methods to perform API related operations',
            'Same as django view, it is epecially used for api',
            'Mapped manually to urls'
        ]
        return Response({'message':apiview})