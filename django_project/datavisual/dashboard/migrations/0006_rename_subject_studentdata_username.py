# Generated by Django 5.0.2 on 2024-03-01 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0005_alter_studentdata_options_alter_studentdata_subject"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentdata",
            old_name="subject",
            new_name="username",
        ),
    ]
