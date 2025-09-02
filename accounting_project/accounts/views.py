from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.shortcuts import render
from .models import Group, Level, AccountMaster
from .serializers import GroupSerializer, LevelSerializer, AccountMasterSerializer

# API views using DRF
class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class AccountMasterListCreateView(generics.ListCreateAPIView):
    queryset = AccountMaster.objects.all()
    serializer_class = AccountMasterSerializer

# HTML dashboard view
def dashboard(request):
    levels = Level.objects.select_related('group').all()
    accounts = AccountMaster.objects.select_related('level').all()
    return render(request, 'dashboard.html', {
        'levels': levels,
        'accounts': accounts
    })
