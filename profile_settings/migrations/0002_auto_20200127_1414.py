# Generated by Django 3.0.1 on 2020-01-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinstagramusersettings',
            name='feedback_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cinstagramusersettings',
            name='news_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cinstagramusersettings',
            name='prodcut_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cinstagramusersettings',
            name='remainder_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cinstagramusersettings',
            name='sms_notifications',
            field=models.BooleanField(default=False),
        ),
    ]