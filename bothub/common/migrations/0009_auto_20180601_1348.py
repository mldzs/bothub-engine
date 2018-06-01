# Generated by Django 2.0.2 on 2018-06-01 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0008_auto_20180529_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(1, 'Up'), (-1, 'Down'), (0, 'Neutral')], verbose_name='vote')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='common.Repository')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'repository vote',
                'verbose_name_plural': 'repository votes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='repositoryvote',
            unique_together={('user', 'repository')},
        ),
    ]
