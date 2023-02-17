# Generated by Django 4.1.3 on 2023-02-16 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colonne_id', models.IntegerField()),
                ('value', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enregistrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universaldjango.donnee')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universaldjango.donnee')),
                ('origine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universaldjango.enregistrement')),
            ],
        ),
        migrations.CreateModel(
            name='Colonne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universaldjango.donnee')),
            ],
        ),
    ]