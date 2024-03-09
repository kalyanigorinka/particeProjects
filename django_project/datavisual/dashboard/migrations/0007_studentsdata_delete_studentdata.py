# Generated by Django 5.0.2 on 2024-03-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_rename_subject_studentdata_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentsData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("percentage", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="StudentData",
        ),
    ]
