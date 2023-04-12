from django import forms
# from django.forms import inlineformset_factory
from user.models import Post
from courses.models import Course, Tag, Prerequisite, Learning, Video
from store.models import Product
from freelance.models import Freelance, Projects

class AddblogForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content':forms.Textarea(attrs={'rows':5, 'cols':50})
        }
        fields = ('title','slug','content','image','status')

class AddcourseForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets = {
            'description':forms.Textarea(attrs={'rows':5, 'cols':50})
        }
        fields = ('name','slug','description','price','discount','active','thumbnail','length')

class AddtagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('description',)

class AddprerequisiteForm(forms.ModelForm):
    class Meta:
        model = Prerequisite
        fields = ('description',)

class AddlearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = ('description',)

class AddvideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'serial_number', 'video_id', 'is_preview')

class AddproductForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'description':forms.Textarea(attrs={'rows':5, 'cols':50})
        }
        fields = ('name','price','description','slug','image','category')

class AddfreelanceForm(forms.ModelForm):
    class Meta:
        model = Freelance
        widgets = {
            'description':forms.Textarea(attrs={'rows':5, 'cols':50})
        }
        fields = ('thumbnail','title','description','slug')

class AddprojectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('skills','projects_done')