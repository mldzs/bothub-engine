# Generated by Django 2.1.11 on 2019-11-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0038_auto_20191101_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='use_analyze_char',
            field=models.BooleanField(default=False, help_text='When selected, the algorithm will learn the patterns of individual characters instead of whole words. This approach works better for some languages.', verbose_name='Use analyze char'),
        ),
    ]
