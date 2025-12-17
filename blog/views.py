from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Gear, Bike
from .forms import ContactMessageForm
from django.utils import timezone

# Home page view
def home(request):
    # Show latest 12 published posts
    posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')[:12]
    
    # All gear items
    gear = Gear.objects.all()
    
    # Latest 4 bikes
    bikes = Bike.objects.all().order_by('-id')[:4]  # assuming 'id' or 'created' gives newest first
    
    return render(request, 'home.html', {'posts': posts, 'gear': gear, 'bikes': bikes})

# Blog listing page
def blog(request):
    blogs = Post.objects.filter(published__lte=timezone.now()).order_by('-published')
    return render(request, 'blogs.html', {'blogs': blogs})

# Individual post detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})

# About page
def about(request):
    return render(request, 'about.html')

# Gear page
def gear(request):
    gear = Gear.objects.all()
    return render(request, 'gear.html', {'gear': gear})

# Bikes page
def bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes.html', {'bikes': bikes})

# Contact page
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})
