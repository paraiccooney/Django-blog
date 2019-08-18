from django.contrib import admin
from .models import Post

# we're allowing our Post model to be accessable from
# the admin backend
admin.site.register(Post)