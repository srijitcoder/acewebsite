# Generated by Django 2.0.4 on 2018-07-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_achievements_calendar_event_photo_projects_upevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='dept',
            field=models.CharField(default='BCA', max_length=6),
        ),
        migrations.AddField(
            model_name='members',
            name='enrollment_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
