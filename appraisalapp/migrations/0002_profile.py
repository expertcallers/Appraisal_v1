# Generated by Django 4.0.1 on 2022-01-11 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appraisalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_desi', models.CharField(max_length=200)),
                ('emp_rm1', models.CharField(max_length=200)),
                ('emp_rm2', models.CharField(max_length=200)),
                ('emp_rm3', models.CharField(max_length=200)),
                ('emp_process', models.CharField(max_length=200)),
                ('emp_doj', models.DateField()),
                ('level', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
