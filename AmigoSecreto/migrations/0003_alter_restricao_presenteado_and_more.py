# Generated by Django 5.0.6 on 2024-05-24 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmigoSecreto', '0002_remove_restricao_grupo_remove_restricao_presenteado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restricao',
            name='presenteado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restricao_presenteado', to='AmigoSecreto.participante'),
        ),
        migrations.AlterField(
            model_name='restricao',
            name='presenteador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restricao_presenteador', to='AmigoSecreto.participante'),
        ),
        migrations.AlterField(
            model_name='sorteio',
            name='presenteado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteio_presenteado', to='AmigoSecreto.participante'),
        ),
        migrations.AlterField(
            model_name='sorteio',
            name='presenteador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorteio_presenteador', to='AmigoSecreto.participante'),
        ),
    ]
