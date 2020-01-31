from . import views
from django.urls import path
app_name = 'examapp'

urlpatterns = [
    path('', views.fn_index, name="index"),
    path('admin_home/', views.fn_login, name="admin_home"),
    path('reg_student/', views.fn_reg_, name="admin_home"),
    # path('student_home/', views.fn_student_home, name="student_home"),

]
