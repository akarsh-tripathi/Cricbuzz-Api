# Generated by Django 5.0.4 on 2024-04-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_alter_matchtable_squad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchtable',
            name='squad',
            field=models.JSONField(default=dict, null=True),
        ),
    ]