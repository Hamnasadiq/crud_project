from django.urls import path
from .views.level_views import (
    level_list,
    level_create,
    level_edit,
    level_delete,
)
from .views.chart_of_accounts_views import (
    chart_of_accounts_list,
    chart_of_accounts_create,
    chart_of_accounts_edit,
    chart_of_accounts_delete,
)

urlpatterns = [
    # Level URLs
    path('levels/', level_list, name='level_list'),  # List all levels
    path('levels/create/', level_create, name='level_create'),  # Create a new level
    path('levels/edit/<int:id>/', level_edit, name='level_edit'),  # Edit an existing level
    path('levels/delete/<int:id>/', level_delete, name='level_delete'),  # Delete a level

    # Chart of Accounts URLs
    path('chart_of_accounts/', chart_of_accounts_list, name='chart_of_accounts_list'),  # List all accounts
    path('chart_of_accounts/create/', chart_of_accounts_create, name='chart_of_accounts_create'),  # Create a new account
    path('chart_of_accounts/edit/<int:id>/', chart_of_accounts_edit, name='chart_of_accounts_edit'),  # Edit an existing account
    path('chart_of_accounts/delete/<int:id>/', chart_of_accounts_delete, name='chart_of_accounts_delete'),  # Delete an account
]