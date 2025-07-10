from django.shortcuts import render
from rest_framework import viewsets, filters, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.


class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    max_page_size = 20


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = UserPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')

        if id:
            queryset = queryset.filter(id=id)
        return queryset


class UserRegisterView(APIView):
    serializer_class = serializers.UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Registration Successful.',
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class = serializers.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Logged Out Successfully.'})
        except:
            return Response({'detail': 'Something went wrong.'})
