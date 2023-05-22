# Generated by Django 4.2.1 on 2023-05-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numero_documento', models.IntegerField(unique=True)),
                ('fecha_alta', models.DateTimeField()),
                ('activo', models.BooleanField(default=1)),
            ],
        ),
    ]
