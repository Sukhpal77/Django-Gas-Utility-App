from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm, CustomUserCreationForm
from .models import ServiceRequest


# 🔑 Custom Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    pending_requests = ServiceRequest.objects.filter(customer=request.user, status="pending").count()
    in_progress_requests = ServiceRequest.objects.filter(customer=request.user, status="in_progress").count()
    completed_requests = ServiceRequest.objects.filter(customer=request.user, status="resolved").count()
    
    recent_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-submitted_at')[:5]
    
    all_requests = ServiceRequest.objects.filter(customer=request.user)

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  
            service_request.save()
            return redirect('home') 
    else:
        form = ServiceRequestForm()  

    return render(request, 'services/home.html', {
        'pending_requests': pending_requests,
        'in_progress_requests': in_progress_requests,
        'completed_requests': completed_requests,
        'recent_requests': recent_requests,
        'requests': all_requests,
        'form': form,
    })

