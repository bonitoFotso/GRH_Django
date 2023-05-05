from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("cre", EmployerCreateView.as_view(), name="emp_creat"),
    path("<int:pk>/up", EmployerUpdateView.as_view(), name="emp_upd"),
    path("<int:pk>/del", EmployerDeleteView.as_view(), name="emp_del"),
    path("list", EmployerList.as_view(), name="list"),
    path('<int:pk>',EmployerDetail.as_view(),name='emp_detail')
    
]
