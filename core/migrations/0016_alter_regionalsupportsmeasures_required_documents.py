# Generated by Django 5.0.6 on 2024-06-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0015_alter_regionalsupportsmeasures_requirements_for_the_applicant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="regionalsupportsmeasures",
            name="required_documents",
            field=models.CharField(max_length=16000, null=True),
        ),
    ]
