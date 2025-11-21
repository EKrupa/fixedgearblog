
from django.contrib import admin
from django.urls import path
from blog.views import home, post_detail, about, gear, blog, contact, bikes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('about/', about, name='about'),
    path('gear/', gear, name='gear'),
    path('blogs/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('bikes/', bikes, name='bikes'),
]
