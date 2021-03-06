# Generated by Django 3.2.5 on 2021-08-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('block', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('x_coordinate', models.DecimalField(decimal_places=4, max_digits=50)),
                ('y_coodinate', models.DecimalField(decimal_places=4, max_digits=50)),
            ],
        ),
    ]
