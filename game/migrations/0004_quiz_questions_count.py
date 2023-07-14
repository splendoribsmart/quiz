# Generated by Django 4.2.3 on 2023-07-11 01:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_point_score_point_general_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='questions_count',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(3)]),
        ),
    ]