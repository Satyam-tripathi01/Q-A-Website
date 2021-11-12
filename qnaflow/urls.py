from django.urls import path
from . import views

urlpatterns=[
path('postq',views.postq,name="postq")
]