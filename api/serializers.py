
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from user.models import CustomUser, Athlete, Sponsor
from donation.models import Donation

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'full_name',
            'role',
            'groups',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        if confirm_password and validated_data['password'] != confirm_password:
            raise serializers.ValidationError("Passwords do not match")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ["full_name","email","password","achievements","age","gender"]

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'




