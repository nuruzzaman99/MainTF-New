# Generated by Django 3.2.7 on 2021-11-02 04:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0005_order_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('new', 'New'), ('attending', 'Attending'), ('on_progress', 'On Progress'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='new', max_length=250),
        ),
    ]
