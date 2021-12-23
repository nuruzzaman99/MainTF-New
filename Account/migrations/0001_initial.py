# Generated by Django 3.2.7 on 2021-12-12 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('address_one', models.CharField(blank=True, max_length=255)),
                ('address_two', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('profile_pic', models.ImageField(default='users/default.jpg', upload_to='users/')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, verbose_name='Choose Gender')),
                ('is_staff', models.BooleanField(default=False, help_text='Designate if the user has staff status', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, help_text='Designate if the user has active status', verbose_name='Active Status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designate if the user has superuser status', verbose_name='Superuser Status')),
                ('is_sales_head', models.BooleanField(default=False, help_text='Designate if the user is sales head ', verbose_name='Sales Head Status')),
                ('is_sales', models.BooleanField(default=False, help_text='Designate if the user is sales', verbose_name='Sales Status')),
                ('is_blogger', models.BooleanField(default=False, help_text='Designate if the user is Blog Admin ', verbose_name='Blog Admin Status')),
                ('is_bcs_head', models.BooleanField(default=False, help_text='Designate if the user is BCS Admin', verbose_name='BCS Admin Status')),
                ('is_pcs_head', models.BooleanField(default=False, help_text='Designate if the user is PCS Admin', verbose_name='PCS Admin Status')),
                ('is_bcs', models.BooleanField(default=False, help_text='Designate if the user is associated with a business', verbose_name='Business Status')),
                ('newsletter', models.BooleanField(default=False, help_text='Receive Email About Update and Notifications', verbose_name='Newsletter')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_type', models.CharField(choices=[('main_admin', 'Main Admin'), ('bcs_admin', 'BCS Admin'), ('pcs_admin', 'PCS Admin'), ('academy_admin', 'Academy Admin'), ('blog_admin', 'Blog Admin')], max_length=264)),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Super Admin')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='Moderator')),
                ('is_editor', models.BooleanField(default=False, verbose_name='Editor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='permission_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_assessment', models.BooleanField(default=True)),
                ('incident_response', models.BooleanField(default=True)),
                ('cyber_crime_investigation', models.BooleanField(default=True)),
                ('open_source_intelligence', models.BooleanField(default=True)),
                ('hack_recovery', models.BooleanField(default=True)),
                ('virus_removal', models.BooleanField(default=True)),
                ('digital_forensic', models.BooleanField(default=True)),
                ('digital_integration', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='interest_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
