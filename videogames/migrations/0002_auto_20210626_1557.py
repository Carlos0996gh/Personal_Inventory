# Generated by Django 3.2.4 on 2021-06-26 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='developer_fundation_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='developer_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videogames.game_format'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videogames.game_status'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videogames.game_genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='purchase_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videogames.purchase_status'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform_release_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_fundation_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
