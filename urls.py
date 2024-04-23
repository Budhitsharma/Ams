from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myAttendance/', views.myAttendance, name='myAttendance'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('colleagues/', views.colleagues, name='colleagues'),
    path('employeeList/', views.employeeList, name='employeeList'),
    path('requestedLeave/', views.requestedLeave, name='requestedLeave'),
    path('statusofLeave/', views.statusofLeave, name='statusofLeave'),
    path('leaveDetails/', views.leaveDetails, name='leaveDetails'),
    path('leaveApplication/', views.leaveApplication, name='leaveApplication'),
    path('employeesLeave/', views.employeesLeave, name='employeesLeave'),
    path('employeeDetails/<int:user_id>/', views.employeeDetails, name='employeeDetails'),
    path('employeeAttendance/', views.employeeAttendance, name='employeeAttendance'),
    path('editEmployeesProfile/<int:user_id>/', views.editEmployeesProfile, name='editEmployeesProfile'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
]