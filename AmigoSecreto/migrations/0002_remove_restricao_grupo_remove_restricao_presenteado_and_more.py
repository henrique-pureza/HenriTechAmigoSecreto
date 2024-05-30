# Generated by Django 5.0.6 on 2024-05-24 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmigoSecreto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restricao',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='restricao',
            name='presenteado',
        ),
        migrations.RemoveField(
            model_name='restricao',
            name='presenteador',
        ),
        migrations.RemoveField(
            model_name='sorteio',
            name='grupo',
        ),
        migrations.AddField(
            model_name='restricao',
            name='grupo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='restricao_grupo', to='AmigoSecreto.grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restricao',
            name='presenteado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='restricao_presenteado', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restricao',
            name='presenteador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='restricao_presenteador', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sorteio',
            name='grupo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sorteio_grupo', to='AmigoSecreto.grupo'),
            preserve_default=False,
        ),
    ]
