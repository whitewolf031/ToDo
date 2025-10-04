from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
import re

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate_password(self, value):
        min_len = 8
        if len(value) < min_len:
            raise serializers.ValidationError(f"Parol kamida {min_len} belgidan iborat bo'lishi kerak")

        if not re.match(r"^[A-Za-z0-9]+$", value):
            raise serializers.ValidationError("Parol faqat harflar va raqamlardan iborat bo'lishi kerak")
        
        if not re.search(r"[A-Za-z]", value) or not re.search(r"\d", value):
            raise serializers.ValidationError("Parol kamida bitta harf va bitta raqamdan iborat bo'lishi kerak")

        return value

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "Parol bir xil emas"})
        self.validate_password(attrs.get("password"))
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2", None)
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()