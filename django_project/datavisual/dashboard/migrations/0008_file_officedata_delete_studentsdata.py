# Generated by Django 5.0.2 on 2024-03-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_studentsdata_delete_studentdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="file",
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
                ("file", models.FileField(upload_to="your_upload_directory/")),
            ],
        ),
        migrations.CreateModel(
            name="OfficeData",
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
                ("date", models.DateTimeField()),
                ("username", models.CharField(max_length=255)),
                ("system_id", models.FloatField()),
                ("test_tab_ref", models.CharField(max_length=255)),
                ("set_power", models.FloatField()),
                ("pos_angle", models.FloatField()),
                ("signal_cat", models.CharField(max_length=255)),
                ("pw", models.FloatField()),
                ("pri", models.FloatField()),
                ("ampl", models.FloatField()),
                ("rms_error", models.FloatField()),
                ("test_status", models.CharField(max_length=255)),
                ("remarks", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="StudentsData",
        ),
    ]
