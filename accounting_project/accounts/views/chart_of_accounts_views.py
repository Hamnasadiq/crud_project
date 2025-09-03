from django.shortcuts import render, redirect, get_object_or_404
from ..models.chart_of_account import ChartOfAccount
from ..forms.chart_of_accounts_form import ChartOfAccountForm

def chart_of_accounts_list(request):
    accounts = ChartOfAccount.objects.all()
    return render(request, 'accounts/chart_of_accounts_list.html', {'accounts': accounts})

def chart_of_accounts_create(request):
    if request.method == 'POST':
        form = ChartOfAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chart_of_accounts_list')
    else:
        form = ChartOfAccountForm()
    return render(request, 'accounts/chart_of_accounts_form.html', {'form': form})

def chart_of_accounts_edit(request, id):
    account = get_object_or_404(ChartOfAccount, id=id)
    if request.method == 'POST':
        form = ChartOfAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('chart_of_accounts_list')
    else:
        form = ChartOfAccountForm(instance=account)
    return render(request, 'accounts/chart_of_accounts_form.html', {'form': form})

def chart_of_accounts_delete(request, id):
    account = get_object_or_404(ChartOfAccount, id=id)
    account.delete()
    return redirect('chart_of_accounts_list')