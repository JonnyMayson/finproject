
from django.db import models


class Task(models.Model):
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.PositiveIntegerField('Age')
    course =  models.PositiveIntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    my_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    ('3', 'I want to learn to play'),
    )
    choice = models.CharField(('Can you play dombyra'),max_length=30,blank=True,null=True,choices=my_choices)
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    kyu_choices=(
    ('1' , 'Ерке Сылқым'),
    ('2' , 'Адай'),
    ('3', 'Сарыарқа'),
    ('4', 'Балбырауын'),
    )
    select_kyu = models.CharField(('Select your known kyu'),max_length=30,choices=kyu_choices,default='1')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user

    class Meta:
        ordering = ['complete']


class Task_music(models.Model):
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.PositiveIntegerField('Age')
    course =  models.PositiveIntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    my_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    ('3', ' I can play an instrument'),
    )
    music = models.CharField(('Can you sing songs ? '),max_length=30,blank=True,null=True,choices=my_choices)
    instrument = models.CharField(('If you play an instrument,which one?'),max_length=50,default='guitar')
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user     




class Task_art(models.Model):
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.PositiveIntegerField('Age')
    course =  models.PositiveIntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    art_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    ('3', ' I want to  learn'),
    )
    art = models.CharField(('Can you draw ? '),max_length=30,blank=True,null=True,choices=art_choices)
    image = models.ImageField(('Your works'),upload_to='blog')
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user  




class Task_vision(models.Model):
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.PositiveIntegerField('Age')
    course =  models.PositiveIntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    vision_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    )
    vision = models.CharField(('Have you ever been a volunteer for a charity ? '),max_length=30,blank=True,null=True,choices=vision_choices)
    cause = models.CharField(('If yes,then what was it like?'),max_length=2000)
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user    

class Task_debate(models.Model):
    fullname_user =models.CharField(('Name and Surname'),max_length = 500)
    year_old = models.PositiveIntegerField('Age')
    course =  models.PositiveIntegerField() 
    email = models.EmailField(('email'), null=True, blank=True)
    debate_choices=(
    ('1' , 'Yes, I can'),
    ('2' , 'No, I can not'),
    )
    debate = models.CharField(('Have you ever played ? '),max_length=30,blank=True,null=True,choices=debate_choices)
    language_choices=(
    ('1' , 'Kazakh'),
    ('2' , 'Russian'),
    ('3' , 'Turkish'),
    )
    debate = models.CharField(('Please,select language that for you comfortable'),max_length=30,blank=True,null=True,choices=language_choices)
    description = models.TextField(('Your other skills and some facts'),null=True,blank = True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname_user    


class Head(models.Model):
    login = models.CharField(max_length=100)
    password =models.CharField(max_length=100) 



from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model): 
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self): 
        return reverse('home') 



class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    title_tag = models.CharField(max_length=1000, default="SDU BLOG")
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length = 255, default = 'DebateClub')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank =True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')    


