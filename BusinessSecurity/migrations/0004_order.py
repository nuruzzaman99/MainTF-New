# Generated by Django 3.2.7 on 2021-11-01 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BusinessSecurity', '0003_usersubserviceinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('new', 'New'), ('following', 'Following'), ('on_progress', 'On Progress'), ('delivered', 'Delivered')], default='new', max_length=250)),
                ('subserviceinput', models.ManyToManyField(related_name='order_subservice', to='BusinessSecurity.UserSubserviceInput')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]