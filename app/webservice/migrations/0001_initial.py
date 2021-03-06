# Generated by Django 4.0.2 on 2022-02-03 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vps',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpu', models.PositiveSmallIntegerField(verbose_name='количество ядер')),
                ('ram', models.PositiveSmallIntegerField(verbose_name='объем RAM')),
                ('hdd', models.PositiveSmallIntegerField(verbose_name='объем HDD')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'stopped'), (1, 'started'), (2, 'blocked')], verbose_name='статус сервера (started, blocked, stopped)')),
            ],
            options={
                'verbose_name': 'VPS',
                'verbose_name_plural': 'VPS',
            },
        ),
    ]
