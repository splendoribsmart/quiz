# Generated by Django 4.2.3 on 2023-07-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='passing_score',
            field=models.PositiveIntegerField(default=17),
        ),
    ]
