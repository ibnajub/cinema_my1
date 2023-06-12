# Generated by Django 4.2 on 2023-06-12 18:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('money', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000)),
                ('number_of_seats', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CinemaSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('movie_show_starts', models.DateTimeField()),
                ('movie_show_ends', models.DateTimeField()),
                ('empty_seats', models.PositiveIntegerField()),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cinema.cinemahall')),
            ],
            options={
                'ordering': ['title', 'movie_show_starts'],
            },
        ),
        migrations.CreateModel(
            name='MovieSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000, null=True)),
                ('img_url', models.ImageField(upload_to='')),
                ('ticket_price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('movie_show_time_starts', models.TimeField()),
                ('movie_show_time_ends', models.TimeField()),
                ('movie_session_start_date', models.DateField()),
                ('movie_session_end_date', models.DateField()),
            ],
            options={
                'ordering': ['movie_session_start_date'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('summ', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cinema_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cinema.cinemasession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='cinemasession',
            name='movie_season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cinema.movieseason'),
        ),
        migrations.AlterUniqueTogether(
            name='cinemasession',
            unique_together={('movie_season', 'cinema_hall', 'movie_show_starts')},
        ),
    ]
