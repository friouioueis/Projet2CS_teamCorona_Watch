# Generated by Django 3.0.4 on 2020-04-08 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compteutilisateur',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]