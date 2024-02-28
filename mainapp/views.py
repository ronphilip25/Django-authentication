from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):         # Main Screen
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})