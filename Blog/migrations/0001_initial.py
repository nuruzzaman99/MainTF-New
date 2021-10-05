# Generated by Django 3.2.7 on 2021-10-04 07:42

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.CharField(max_length=264, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=264, verbose_name='Add Title')),
                ('category', models.CharField(choices=[('blogs', 'Blog'), ('case_studies', 'Case Study'), ('podcast', 'Podcast')], default='blogs', max_length=100)),
                ('feature_image', models.ImageField(upload_to='blog/', verbose_name='Add Feature Image')),
                ('shot_description', models.TextField(max_length=264, verbose_name='Short Description')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Post Content')),
                ('reading_time', models.DurationField(default=datetime.timedelta(seconds=180))),
                ('comment_option', models.CharField(choices=[('disabled', 'Disable Comments'), ('enabled', 'Enable Comments')], default='disabled', max_length=100)),
                ('tag', models.CharField(max_length=264)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('sub_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_sub_category', to='Blog.subcategory')),
            ],
        ),
    ]
