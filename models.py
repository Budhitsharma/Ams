from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.
class EmployeeDetailmodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField(null=True, blank=True)
    Gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=Gender, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    aadhar_no = models.IntegerField(null=True, blank=True)
    pan_no = models.CharField(max_length=15)
    skype_id = models.CharField(max_length=50)
    linkedin_id = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=500, default='')
    qualification = models.CharField(max_length=50, default='')
    technology = models.CharField(max_length=50, default='')
    perv_company = models.CharField(max_length=50, default='')
    experience = models.IntegerField(null=True, blank=True)
    acc_no = models.IntegerField(null=True, blank=True)
    acc_name = models.CharField(max_length=30, default='')
    bank_name = models.CharField(max_length=30, default='')
    ifsc_code = models.CharField(max_length=15, default='')
    image = models.ImageField(upload_to="myapp/images/", max_length=250, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.user.username}'s Details"

class Timemodel(models.Model):
    employee = models.ForeignKey(EmployeeDetailmodel, on_delete=models.CASCADE)
    date_field = models.DateField(default=date.today)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    break_start = models.TimeField(null=True, blank=True)
    break_end = models.TimeField(null=True, blank=True)

    duration = models.DurationField(null=True, blank=True)
    break_duration = models.DurationField(null=True, blank=True)
    working_hour = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.employee.user.username
    
class Leavemodel(models.Model):
    Leave_Type = [
        ('gen', 'General Leave'),
        ('med', 'Medical Leave'),
        ('wfh', 'Work From Home'),
        ('oth', 'Other'),
    ]
    employee = models.ForeignKey(EmployeeDetailmodel, on_delete=models.CASCADE)
    apply_date = models.DateField()
    leave_type = models.CharField(max_length=3, choices=Leave_Type, null=True, blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=250)
    

    def __str__(self):
        return self.employee.user.username