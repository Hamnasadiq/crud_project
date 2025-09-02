from rest_framework import serializers
from .models import Group, Level, AccountMaster

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_id', 'group_title']


class LevelSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), source='group', write_only=True
    )

    class Meta:
        model = Level
        fields = ['lev_id', 'lev_title', 'pre_id', 'group', 'group_id']


class AccountMasterSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    level_id = serializers.PrimaryKeyRelatedField(
        queryset=Level.objects.all(), source='level', write_only=True
    )

    class Meta:
        model = AccountMaster
        fields = ['acc_id', 'acc_title', 'level', 'level_id']
