# Generated by Django 5.0.4 on 2024-04-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_playerssquadtable_remove_matchtable_squad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchtable',
            name='match_date',
            field=models.CharField(max_length=100),
        ),
    ]
