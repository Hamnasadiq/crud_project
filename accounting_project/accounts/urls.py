from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/', views.account_details, name='account-details'),

    # API endpoints (optional)
    path('api/groups/', views.GroupListCreateView.as_view(), name='group-list'),
    path('api/groups/<int:pk>/', views.GroupRetrieveUpdateDestroyView.as_view(), name='group-detail'),
    path('api/levels/', views.LevelListCreateView.as_view(), name='level-list'),
    path('api/levels/<int:pk>/', views.LevelRetrieveUpdateDestroyView.as_view(), name='level-detail'),
    path('api/accounts/', views.AccountListCreateView.as_view(), name='account-list'),
    path('api/accounts/<int:pk>/', views.AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),
]
