from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import EmailSignUpSerailzier
# from .models import MyUser
# from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class UserSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmailSignUpSerailzier

    def post(self, request, *args, **kwargs):
        try:
            serializer = EmailSignUpSerailzier(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
                # user = MyUser.objects.get(email=serializer.data.get('email'))
                # refresh = RefreshToken.for_user(user)
            return Response({"status": True, "message": "User Registered Successfully", "data": serializer.data})
        except Exception as e:
            error = {"status": False, "message": e.args[0]}
            return Response(error)



