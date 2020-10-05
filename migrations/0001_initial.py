# Generated by Django 2.1.4 on 2018-12-10 14:06

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import toplanti.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('organizations', djongo.models.fields.ArrayModelField(model_container=toplanti.models.OrganizasyonTutucu)),
                ('rols', djongo.models.fields.ArrayModelField(model_container=toplanti.models.OrganizasyonTutucu)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizasyonTutucu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roller', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='organizasyontutucu',
            name='organizasyon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toplanti.Organization'),
        ),
        migrations.AddField(
            model_name='organizasyontutucu',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toplanti.Role'),
        ),
    ]
