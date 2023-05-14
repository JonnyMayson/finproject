# Generated by Django 4.0.2 on 2022-04-21 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0012_remove_head_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
