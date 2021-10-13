# Generated by Django 3.2.7 on 2021-10-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_permissions_admin_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='admin_type',
            field=models.CharField(choices=[('main_admin', 'Main Admin'), ('bcs_admin', 'BCS Admin'), ('pcs_admin', 'PCS Admin'), ('academy_admin', 'Academy Admin'), ('blog_admin', 'Blog Admin')], max_length=264),
        ),
    ]