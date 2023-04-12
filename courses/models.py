from django.db import models
from store.models import Customer
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True, help_text='This field should be unique')
    description = models.TextField(null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to = "thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    # resource = models.FileField(upload_to = "resources", null=True, blank=True)
    length = models.IntegerField(null=False)
    seller = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
	    ordering = ('-date',)

    def __str__(self):
        return self.name

    @property
    def thumbnailURL(self):
    	try:
    		url = self.thumbnail.url
    	except:
    		url = ''
    	return url


class CourseProperty(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100, null=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class UserCourse(models.Model):
    user = models.ForeignKey(Customer, null = False , on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} - {self.course.name}'

class Payment(models.Model):
    order_id = models.CharField(max_length = 50, null = False)
    payment_id = models.CharField(max_length = 50)
    user_course = models.ForeignKey(UserCourse , null = True, blank = True,  on_delete=models.CASCADE)
    user = models.ForeignKey(Customer,  on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
