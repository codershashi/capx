# Generated by Django 4.2.6 on 2023-10-29 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='100 characters or fewer', max_length=100, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='date joined')),
                ('groups', models.JSONField(null=True)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(error_messages={'unique': "There's another organization with that name."}, max_length=256, unique=True, verbose_name='Organization name')),
                ('organization_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Organization code')),
                ('organization_website', models.URLField(error_messages={'unique': 'This website is already used by another organization.'}, unique=True, verbose_name='Organization website')),
            ],
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=128, verbose_name='Area name')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=128, verbose_name='Language name')),
                ('language_code', models.CharField(max_length=10, unique=True, verbose_name='Language code')),
            ],
        ),
        migrations.CreateModel(
            name='WikimediaProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wikimedia_project_name', models.CharField(max_length=128, verbose_name='Wikimedia project name')),
                ('wikimedia_project_code', models.CharField(max_length=40, unique=True, verbose_name='Wikimedia project code')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=128, unique=True, verbose_name='Region name')),
                ('parent_region', models.ManyToManyField(blank=True, related_name='region_parent', to='users.region', verbose_name='Parent region')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.JSONField(blank=True, null=True, verbose_name='Groups')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, verbose_name='Username')),
                ('pronoun', models.CharField(blank=True, choices=[('he-him', 'He/Him'), ('she-her', 'She/Her'), ('they-them', 'They/Them')], max_length=20, null=True, verbose_name='Pronoun')),
                ('profile_image', models.URLField(blank=True, null=True, verbose_name='Profile image')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Last name')),
                ('display_name', models.CharField(blank=True, max_length=387, null=True, verbose_name='Display name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('twitter', models.CharField(blank=True, max_length=128, null=True, verbose_name='Twitter handle')),
                ('facebook', models.CharField(blank=True, max_length=128, null=True, verbose_name='Facebook handle')),
                ('instagram', models.CharField(blank=True, max_length=128, null=True, verbose_name='Instagram handle')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'This email is already in use.'}, max_length=254, null=True, unique=True)),
                ('contact_method', models.CharField(blank=True, choices=[('email', 'Email'), ('wiki', 'Discussion page')], max_length=10, null=True, verbose_name='Preferred contact method')),
                ('affiliation', models.ManyToManyField(blank=True, related_name='user_affiliation', to='users.affiliation', verbose_name='Affiliation')),
                ('area_of_interest', models.ManyToManyField(blank=True, related_name='user_area_of_interest', to='users.areaofinterest', verbose_name='Area of interest')),
                ('language', models.ManyToManyField(blank=True, related_name='user_language', to='users.language', verbose_name='Language')),
                ('region', models.ManyToManyField(blank=True, related_name='user_region', to='users.region', verbose_name='Region')),
                ('skills_known', models.ManyToManyField(blank=True, related_name='user_skils', to='skills.skill', verbose_name='Skill known')),
                ('skills_wanted', models.ManyToManyField(blank=True, related_name='user_desired_skils', to='skills.skill', verbose_name='Skill desired')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wikimedia_project', models.ManyToManyField(blank=True, related_name='user_wikimedia_project', to='users.wikimediaproject', verbose_name='Wikimedia project')),
            ],
        ),
    ]