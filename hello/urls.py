
from .views import AddCategoryView, ArticleDetailView, CategoryView,TaskCreate,TaskCreateMusic,TaskCreateArt,TaskCreateVision,TaskCreateDebate, dombyra,music, logout_user
from .views import index
from django.urls import path
from .views import HomeView, AddBlogView, UpdatePostView, DeleteViewPost
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('', views.login_user, name='login'),
    path('main/',index, name = 'tasks'),
    path('task-create/' , TaskCreate.as_view(),name='task-create'),
    path('task-music/',TaskCreateMusic.as_view(),name='task-music'),
    path('task-art/',TaskCreateArt.as_view(),name='task-art'),
    path('task-vision/',TaskCreateVision.as_view(),name='task-vision'),
    path('task-debate/',TaskCreateDebate.as_view(),name='task-debate'),
    path('dombyra', dombyra, name ="dombyra"),
    path('music', music, name ="music"),
    path('log_out', logout_user, name = "logout_user"),
    path('minecraft/',views.show_tasks,name = 'minecraft'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('see_blog/', HomeView.as_view(), name="home"),
    path('blog/<int:blog_id>', views.details, name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('blog/<int:pk>/remove', DeleteViewPost.as_view(), name = "delete_post"),
    path('add_category2/', views.create_view, name='add_category2'),


   

]











urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)






    
    
    
    

