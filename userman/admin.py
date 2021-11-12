from django.contrib import admin
from .models import user_login,question_box,answers,hello
# Register your models here.
admin.site.register(user_login)
admin.site.register(question_box)
admin.site.register(answers)
admin.site.register(hello)
