from django.contrib import admin
from .models import Category, Head, Task,Task_music,Task_art,Task_vision,Task_debate,BlogModel

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_music)
admin.site.register(Task_art)
admin.site.register(Task_vision)
admin.site.register(Task_debate)
admin.site.register(Head)
admin.site.register(BlogModel)
admin.site.register(Category)

