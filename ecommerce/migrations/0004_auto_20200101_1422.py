# Generated by Django 2.2.8 on 2020-01-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20191225_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SP', 'Speaker'), ('A', 'Accesories'), ('S', 'Synch')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('P', 'primary')], max_length=1),
        ),
    ]