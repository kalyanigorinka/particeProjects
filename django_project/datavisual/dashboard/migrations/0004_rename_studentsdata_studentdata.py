# Generated by Django 5.0.2 on 2024-03-01 10:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0003_studentsdata_delete_countrydata"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StudentsData",
            new_name="StudentData",
        ),
    ]
