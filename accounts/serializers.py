import re
# accounts/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username','email','password','password2','role')
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': False, 'read_only': True} # Role faqat admin tomonidan belgilanadi
        }

# Password to'griligini tekshirish
    def validate(self, attrs):
        if attrs['password'] !=attrs['password2']:
            return super().validate(attrs)
        
# Email manzil tekshirish
def validate_email(self, data):
    # “Oddiy elektron pochta manzilini tekshirish uchun muntazam ifoda (regex)
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Elektron pochta manzili regex bilan mos kelishini tekshiring.
    if re.match(email_regex, data):
        return True
    else:
        return False

def create(self, validated_data):
        validated_data.pop('password2')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Roles.STUDENT # Yangi ro'yxatdan o'tganlarga default rol
        )
        return user

