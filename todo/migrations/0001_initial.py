# Generated by Django 5.0.1 on 2024-01-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('In progress', 'In progress')], default='pending', max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]