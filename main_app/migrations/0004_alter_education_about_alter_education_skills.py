# Generated by Django 4.1.7 on 2023-04-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_education_skills_alter_experience_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='about',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='education',
            name='skills',
            field=models.CharField(max_length=100),
        ),
    ]