# Generated by Django 5.0.6 on 2024-06-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_alter_regionalsupportsmeasures_main_idea_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialeconomicszonesandtechn",
            name="validation_period_object",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
