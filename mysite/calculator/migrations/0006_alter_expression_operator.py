# Generated by Django 4.1.6 on 2023-03-15 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_alter_expression_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='calculator.operator'),
        ),
    ]
