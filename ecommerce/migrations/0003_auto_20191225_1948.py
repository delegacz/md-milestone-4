# Generated by Django 2.2.8 on 2019-12-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20191225_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Synch'), ('A', 'Accesories'), ('SP', 'Speaker')], max_length=2),
        ),
    ]
