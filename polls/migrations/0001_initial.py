# Generated by Django 4.2.1 on 2023-05-28 15:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('fecha_ultimo_pago', models.DateField(blank=True, null=True)),
                ('vencimiento_suscripcion', models.DateField(blank=True, null=True)),
                ('estado_suscripcion', models.BooleanField()),
            ],
            options={
                'db_table': 'suscripcion',
            },
        ),
    ]
