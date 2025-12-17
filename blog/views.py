from django.shortcuts import render, redirect
from .models import Post, Gear, Bike
from .forms import ContactMessageForm, CommentForm
from django.utils import timezone


# Create your views here.
def home(request):
    from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Gear, Bike
from .forms import ContactMessageForm
from django.utils import timezone

# Home page view
def home(request):
    # Only show posts that are published (published <= now), newest first, limit 12
    posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')[:12]
    gear = Gear.objects.all()
    # Assuming bikes are also posts with some filter; otherwise use Bike model
    bikes = Post.objects.filter(published__lte=timezone.now()).order_by('-published')[:4]
    return render(request, 'home.html', {'posts': posts, 'gear': gear, 'bikes': bikes})

# Blog listing page
def blog(request):
    from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Gear, Bike
from .forms import ContactMessageForm
from django.utils import timezone

# Home page view
def home(request):
    # Only show posts that are published (published <= now), newest first, limit 12
    posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')[:12]
    gear = Gear.objects.all()
    # Assuming bikes are also posts with some filter; otherwise use Bike model
    bikes = Post.objects.filter(published__lte=timezone.now()).order_by('-published')[:4]
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

    gear = Gear.objects.all()
    bikes = Post.objects.all().order_by('-published')[:4]
    return render(request, 'home.html', {'posts': posts, 'gear': gear, 'bikes': bikes})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')


def gear(request):
    gear = Gear.objects.all()
    return render(request, 'gear.html', {'gear': gear})

def blog(request):
    blogs = Post.objects.all().order_by('-published')
    return render(request, 'blogs.html', {'blogs': blogs})

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ContactMessageForm()
        return render(request, 'contact.html', {'form': form})
    

def bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes.html', {'bikes': bikes})
