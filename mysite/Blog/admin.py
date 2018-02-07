from django.contrib import admin
from .models import Post
from .models import Mail
from .models import account
# Register your models here.
admin.site.register(Post)
admin.site.register(Mail)
admin.site.register(account)
