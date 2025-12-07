from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

#Local files 
from .serializers import UserRegisterSerializer
from .models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny)
    serializer_class = UserRegisterSerializer

class LogoutView(generics.GenericAPIView):
    """
    Foydalanuvchini tizimdan chiqarish (Refresh Tokenni Blacklist qilish).
    """
    permission_classes = (IsAuthenticated,) # Tizimga kirgan bo'lishi kerak

    def post(self, request, *args, **kwargs):
        try:
            # Refresh Tokenni POST so'rovining data qismidan olish
            refresh_token = request.data["refresh_token"] 
            token = RefreshToken(refresh_token)
            token.blacklist() # Tokenni qora ro'yxatga qo'shish

            return Response(
                {"detail": "Tizimdan muvaffaqiyatli chiqildi."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            # Agar Refresh Token noto'g'ri bo'lsa yoki taqdim etilmasa
            return Response(
                {"detail": "Refresh token kiritilmagan yoki noto'g'ri."},
                status=status.HTTP_400_BAD_REQUEST
            )