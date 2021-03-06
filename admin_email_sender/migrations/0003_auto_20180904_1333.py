# Generated by Django 2.1 on 2018-09-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0004_auto_20180815_0229'),
        ('admin_email_sender', '0002_auto_20180904_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail_ACEUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField(help_text='You can use tags:<br>@username<br>@fullName<br>@firstName<br>@lastName')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('members', models.ManyToManyField(related_name='_sendemail_aceuserprofile_members_+', to='portalapp.ACEUserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='sendemail_aceuserprofilecoremembers',
            name='members',
        ),
        migrations.RemoveField(
            model_name='sendemail_aceuserprofilemembers',
            name='members',
        ),
        migrations.DeleteModel(
            name='SendEmail_ACEUserProfileCoreMembers',
        ),
        migrations.DeleteModel(
            name='SendEmail_ACEUserProfileMembers',
        ),
        migrations.CreateModel(
            name='SendEmail_ACEUserProfileCore',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('admin_email_sender.sendemail_aceuserprofile',),
        ),
    ]
