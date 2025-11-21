from django.shortcuts import render, redirect
from .models import Post, Gear, Bike
from .forms import ContactMessageForm, CommentForm


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-published')[:12]
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