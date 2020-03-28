# Generated by Django 3.0.3 on 2020-03-28 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='notifUtilisateur',
            fields=[
                ('idNotif', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('typeNotif', models.CharField(choices=[('zd', 'zone dangereuse'), ('vv', 'video validée'), ('md', 'malade'), ('sg', 'signalement')], max_length=2, verbose_name='type')),
                ('contenuNotif', models.TextField(verbose_name='contenu')),
                ('idUtilisateurNf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
        ),
    ]
