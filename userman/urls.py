from django.urls import path
from . import views
urlpatterns=[
	path('usersignup',views.usersignup,name="usersignup"),
	path('userlogin',views.userlogin,name="userlogin"),
	path('reg',views.reg,name="reg"),
	path('userlog',views.userlog,name="userlog"),
	path('home',views.home,name="home"),
	path('logout',views.logout,name="logout"),
	path('postq',views.postq,name="postq"),
	path('ques',views.ques,name="ques"),
	path('answers',views.answers,name="answers"),
	path('addans',views.addans,name="addans")
]