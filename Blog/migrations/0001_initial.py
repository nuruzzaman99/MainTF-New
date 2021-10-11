# Generated by Django 3.2.7 on 2021-10-11 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=80)),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='subcategory_category', to='Blog.BlogCategory')),
            ],
            options={
                'verbose_name_plural': 'Blog Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='FilterOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=80)),
                ('sub_category', models.ManyToManyField(blank=True, null=True, related_name='filter_subcategory', to='Blog.BlogSubCategory')),
            ],
            options={
                'verbose_name_plural': 'Blog Filter Option',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.CharField(max_length=264, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=264, verbose_name='Add Title')),
                ('feature_image', models.ImageField(upload_to='blog/', verbose_name='Add Feature Image')),
                ('short_description', models.TextField(max_length=264, verbose_name='Short Description')),
                ('content', tinymce.models.HTMLField(verbose_name='Post Content')),
                ('comment_option', models.CharField(choices=[('disabled', 'Disable Comments'), ('enabled', 'Enable Comments')], default='disabled', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('total_view', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='Blog.blogcategory')),
                ('filter_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_filter', to='Blog.filteroption')),
                ('sub_categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_sub_category', to='Blog.blogsubcategory')),
                ('tag', models.ManyToManyField(related_name='post_tags', to='Blog.Tags', verbose_name='Add Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500, verbose_name='Comment')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='Blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
