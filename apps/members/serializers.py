from rest_framework import serializers
from apps.members.models import *

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['member_id','passwd', 'name', 'email','height','weight', 'gender', 'purpose', 'age']




