from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.StudentDetailsView,name="studentsdetails"),
    path('getinfo',views.GetInfoView,name='getinfo'),
    path('getallvalue',views.getAll,name='getall'),
    path('accounts/',include("django.contrib.auth.urls"))

]