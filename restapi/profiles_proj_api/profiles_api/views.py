from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class BaseAPIView(APIView):

    serializer_class=serializers.BaseSerializer

    def get(self,request,format=None):
        apiview=[
            'HTTP methods to perform API related operations',
            'Same as django view, it is epecially used for api',
            'Mapped manually to urls'
        ]
        return Response({'message':apiview})
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello,{name}'
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
