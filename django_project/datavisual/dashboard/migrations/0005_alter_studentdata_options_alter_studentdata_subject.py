# Generated by Django 5.0.2 on 2024-03-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0004_rename_studentsdata_studentdata"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentdata",
            options={},
        ),
        migrations.AlterField(
            model_name="studentdata",
            name="subject",
            field=models.CharField(max_length=50),
        ),
    ]
