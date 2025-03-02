from rest_framework import generics as views, status
from rest_framework.response import Response
from .models import User
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserCreationSerializer


class UserCreateView(views.CreateAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(
            operation_summary='Create a User Account'
        )
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )