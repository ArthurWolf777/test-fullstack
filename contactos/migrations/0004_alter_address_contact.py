# Generated by Django 4.1.6 on 2023-02-16 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_alter_address_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactos.contact'),
        ),
    ]
