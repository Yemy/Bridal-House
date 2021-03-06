# Generated by Django 2.2.7 on 2021-03-07 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='', max_length=1)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Registration', 'Registration'), ('Login', 'Login'), ('Profile', 'Profile'), ('Changing Password', 'Changing Password'), ('Resting Password', 'Reseting Password'), ('Courses', 'Courses'), ('Chapters', 'Chapters'), ('Topics', 'Topics'), ('Other', 'Other')], default='', help_text='choose Which one is not working for you?', max_length=50)),
                ('issue', models.TextField(help_text='write your specific problems that you found.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Issue',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedBack', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'FeedBack',
            },
        ),
    ]
