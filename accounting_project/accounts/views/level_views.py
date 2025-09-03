from django.shortcuts import render, redirect, get_object_or_404
from ..models.level import Level
from ..forms.level_form import LevelForm

def level_list(request):
    levels = Level.objects.all()
    return render(request, 'accounts/level_list.html', {'levels': levels})

def level_create(request):
    if request.method == 'POST':
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('level_list')
    else:
        form = LevelForm()
    return render(request, 'accounts/level_form.html', {'form': form})

def level_edit(request, id):
    level = get_object_or_404(Level, level_id=id)  # Use 'id' here
    if request.method == 'POST':
        form = LevelForm(request.POST, instance=level)
        if form.is_valid():
            form.save()
            return redirect('level_list')  # Redirect to the list view after saving
    else:
        form = LevelForm(instance=level)
    return render(request, 'accounts/level_form.html', {'form': form})

def level_delete(request, id):
    level = get_object_or_404(Level, id=id)
    if request.method == 'POST':  # Ensure it's a POST request for deletion
        level.delete()
        return redirect('level_list')
    return render(request, 'accounts/level_confirm_delete.html', {'level': level})