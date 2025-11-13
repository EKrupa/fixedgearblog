from django.contrib import admin

# Register your models here.
from .models import Post, Gear, ContactMessage

admin.site.register(Post)
admin.site.register(Gear)
admin.site.register(ContactMessage)