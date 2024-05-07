from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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
        
    def put(self,request,pk=None):
        return Response({'message':'PUT used'})

    def patch(self,request,pk=None):
        return Response({'message':'PATCH used'})
    
    def delete(self,request,pk=None):
        return Response({'message':'DELETE used'})
    
class BaseViewSet(viewsets.ViewSet):

    serializer_class=serializers.BaseSerializer

    def list(self,request):
        view_set=[
            'Actions often associated to a list set',
            'Auto mapping to urls via routers',
            'More functiona but usees less code'
        ]
        return Response({'message':view_set})
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data('name')
            msg=f"Hello {name}"
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'message':'RETRIEVE used'})

    def update(self,request,pk=None):
        return Response({'message':'UPDATE used'})  
    
    def partial_update(self,request,pk=None):
        return Response({'message':'PARTIAL UPDATE used'})
    
    def destroy(self,request,pk=None):
        return Response({'message':'DELETE used'})