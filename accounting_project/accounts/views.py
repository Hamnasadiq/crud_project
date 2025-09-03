from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import generics
from .models import Group, Level, AccountMaster
from .serializers import GroupSerializer, LevelSerializer, AccountMasterSerializer

# --- (DRF class-based API views remain unchanged) ---
class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = AccountMaster.objects.all()
    serializer_class = AccountMasterSerializer

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountMaster.objects.all()
    serializer_class = AccountMasterSerializer


# ---------------------------
# Template views
# ---------------------------
def dashboard(request):
    """
    GET: render forms + lists
    POST: handle create_group, create_level, create_account, delete_account,
          delete_group, delete_level
    """
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # CREATE GROUP
        if form_type == 'create_group':
            title = (request.POST.get('group_title') or '').strip()
            if title:
                Group.objects.create(group_title=title)
                messages.success(request, f'Group \"{title}\" created.')
            else:
                messages.error(request, "Group title can't be empty.")
            return redirect('dashboard')

        # CREATE LEVEL (pre_id auto-generated per group)
        if form_type == 'create_level':
            lev_title = (request.POST.get('lev_title') or '').strip()
            group_id = request.POST.get('group_id')
            # get group safely
            try:
                group = Group.objects.get(pk=int(group_id))
            except Exception:
                group = None

            if not lev_title:
                messages.error(request, "Level title is required.")
            elif not group:
                messages.error(request, "Please select a valid Group.")
            else:
                # previous id = last level's id for this group (or None)
                last_level = Level.objects.filter(group=group).order_by('-lev_id').first()
                pre_id = last_level.lev_id if last_level else None
                Level.objects.create(lev_title=lev_title, pre_id=pre_id, group=group)
                messages.success(request, f'Level \"{lev_title}\" created. (pre_id: {pre_id})')
            return redirect('dashboard')

        # CREATE ACCOUNT
        if form_type == 'create_account':
            acc_title = (request.POST.get('acc_title') or '').strip()
            level_id = request.POST.get('level_id')
            try:
                level = Level.objects.get(pk=int(level_id))
            except Exception:
                level = None

            if not acc_title:
                messages.error(request, "Account title is required.")
            elif not level:
                messages.error(request, "Please select a valid Level.")
            else:
                AccountMaster.objects.create(acc_title=acc_title, level=level)
                messages.success(request, f'Account \"{acc_title}\" created.')
            return redirect('dashboard')

        # DELETE ACCOUNT (from dashboard table)
        if form_type == 'delete_account':
            acc_id = request.POST.get('acc_id')
            try:
                acc = AccountMaster.objects.get(pk=int(acc_id))
                acc_name = acc.acc_title
                acc.delete()
                messages.success(request, f'Account \"{acc_name}\" deleted.')
            except Exception:
                messages.error(request, "Could not delete account.")
            return redirect('dashboard')

        # DELETE GROUP
        if form_type == 'delete_group':
            group_id = request.POST.get('group_id')
            try:
                g = Group.objects.get(pk=int(group_id))
                g_name = g.group_title
                g.delete()  # cascades to Levels/Accounts
                messages.success(request, f'Group \"{g_name}\" and its related records deleted.')
            except Exception:
                messages.error(request, "Could not delete group.")
            return redirect('dashboard')

        # DELETE LEVEL
        if form_type == 'delete_level':
            lev_id = request.POST.get('lev_id')
            try:
                l = Level.objects.get(pk=int(lev_id))
                l_name = l.lev_title
                l.delete()  # cascades to AccountMaster due to FK cascade
                messages.success(request, f'Level \"{l_name}\" deleted.')
            except Exception:
                messages.error(request, "Could not delete level.")
            return redirect('dashboard')

    # GET: prepare context
    groups = Group.objects.all().order_by('group_title')
    levels = Level.objects.select_related('group').all().order_by('lev_id')
    accounts = AccountMaster.objects.select_related('level', 'level__group').all().order_by('acc_title')

    context = {
        'groups': groups,
        'levels': levels,
        'accounts': accounts
    }
    return render(request, 'accounts/dashboard.html', context)


def account_details(request):
    """
    Renders account details and accepts account deletion (POST).
    """
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'delete_account':
            acc_id = request.POST.get('acc_id')
            try:
                acc = AccountMaster.objects.get(pk=int(acc_id))
                acc_name = acc.acc_title
                acc.delete()
                messages.success(request, f'Account \"{acc_name}\" deleted.')
            except Exception:
                messages.error(request, "Could not delete account.")
            return redirect('account-details')

    accounts = AccountMaster.objects.select_related('level', 'level__group').all().order_by('acc_title')
    return render(request, 'accounts/account_details.html', {'accounts': accounts})
