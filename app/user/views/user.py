from rest_framework import generics
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user
