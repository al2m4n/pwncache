# Generated by Django 4.0.4 on 2022-04-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_asset_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='contract_address',
            field=models.CharField(max_length=50),
        ),
    ]