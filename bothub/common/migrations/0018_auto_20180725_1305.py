# Generated by Django 2.0.6 on 2018-07-25 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


def populate_example_entities(apps, *args):
    RepositoryExampleEntity = apps.get_model('common', 'RepositoryExampleEntity')
    RepositoryTranslatedExampleEntity = apps.get_model('common', 'RepositoryTranslatedExampleEntity')
    RepositoryEntity = apps.get_model('common', 'RepositoryEntity')

    for e in RepositoryExampleEntity.objects.all():
        entity, create = RepositoryEntity.objects.get_or_create(
            repository=e.repository_example.repository_update.repository,
            value=e.entity)
        e.entity = entity.pk
        e.save()

    for e in RepositoryTranslatedExampleEntity.objects.all():
        entity, create = RepositoryEntity.objects.get_or_create(
            repository=e.repository_translated_example.repository_update.repository,
            value=e.entity)
        e.entity = entity.pk
        e.save()


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_auto_20180712_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Entity name', max_length=64, validators=[django.core.validators.RegexValidator(re.compile('^[-a-z0-9_]+\\Z'), 'Enter a valid value consisting of lowercase letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='entity')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='common.Repository')),
            ],
        ),
        migrations.RunPython(populate_example_entities),
        migrations.AlterField(
            model_name='repositoryexampleentity',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.RepositoryEntity'),
        ),
        migrations.AlterField(
            model_name='repositorytranslatedexampleentity',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.RepositoryEntity'),
        ),
        migrations.AlterUniqueTogether(
            name='repositoryentity',
            unique_together={('repository', 'value')},
        ),
    ]