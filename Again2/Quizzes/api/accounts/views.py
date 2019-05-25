from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import (UserCreateSerializer, UserLoginSerializer)

User = get_user_model()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({'users': reverse('user-list', request=request, format=format),
                     'snippets': reverse('snippet-list', request=request, format=format)})



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserLoginAPIView(APIView):
    # permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
