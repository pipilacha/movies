# Generated by Django 4.2 on 2023-10-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_gender_movies_genders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
