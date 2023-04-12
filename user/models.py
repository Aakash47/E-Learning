from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	options = {
		('draft', 'Draft'),
		('published', 'Published'),
	}
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True, help_text='This field should be unique')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField( upload_to="thumbnail", null=True, blank=True)
	status = models.CharField(max_length=10, choices=options, default='draft')
	
	class Meta:
		ordering = ('-date_posted',)

	def __str__(self):
		return self.title

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['created_on']
	
	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)