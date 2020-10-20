from django.contrib import admin

from user_faq.models import GamefaqUser
from user_faq.models import User_Comments
# Register your models here.

admin.site.register(GamefaqUser)
admin.site.register(User_Comments)
