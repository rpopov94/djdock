# Generated by Django 3.2.5 on 2021-07-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datamap',
            options={'ordering': ['address']},
        ),
        migrations.RenameField(
            model_name='datamap',
            old_name='geo',
            new_name='geoinfo',
        ),
        migrations.RenameField(
            model_name='datamap',
            old_name='schools',
            new_name='shools',
        ),
    ]
