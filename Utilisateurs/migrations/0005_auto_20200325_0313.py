# Generated by Django 3.0.4 on 2020-03-25 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Utilisateurs', '0004_auto_20200325_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopersonel',
            name='idUtilisateurIp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
    ]
