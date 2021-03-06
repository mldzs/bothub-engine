# Generated by Django 2.2.12 on 2020-08-31 18:24

from django.db import migrations


def noop(apps, schema_editor):  # pragma: no cover
    pass


def migration(apps, schema_editor):  # pragma: no cover
    RepositoryNLPLog = apps.get_model("common", "RepositoryNLPLog")
    RepositoryReports = apps.get_model("common", "RepositoryReports")

    for log in (
        RepositoryNLPLog.objects.filter(created_at__gte="2020-09-01")
        .only("repository_version_language", "user", "created_at")
        .iterator()
    ):
        report, created = RepositoryReports.objects.get_or_create(
            repository_version_language=log.repository_version_language,
            user=log.user,
            report_date=log.created_at.date(),
        )
        report.count_reports += 1
        report.save(update_fields=["count_reports"])


class Migration(migrations.Migration):

    dependencies = [("common", "0084_repositoryreports")]

    operations = [migrations.RunPython(migration, noop)]
