# Generated by Django 4.2.1 on 2023-05-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0015_device_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='device',
        ),
        migrations.RemoveField(
            model_name='dbstatus',
            name='device',
        ),
        migrations.AddField(
            model_name='dbstatus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
