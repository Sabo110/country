# Generated by Django 5.0.2 on 2024-02-27 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lespays', '0002_alter_pays_continent_alter_pays_superficie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pays',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pays', to='lespays.continent'),
        ),
    ]
