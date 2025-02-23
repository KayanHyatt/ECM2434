# Generated by Django 5.1.5 on 2025-02-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecolution', '0009_remove_customuser_pet_level_range_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='customuser',
            name='preferred_font_size_range',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='preferred_font_size',
            field=models.PositiveSmallIntegerField(choices=[(13, 'Small'), (16, 'Medium'), (19, 'Large')], default=16),
        ),
    ]
