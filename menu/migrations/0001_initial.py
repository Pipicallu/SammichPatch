# Generated by Django 3.1.7 on 2021-02-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DietaryRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SidesAndDrinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category')),
                ('dietary_requirements', models.ManyToManyField(to='menu.DietaryRequirements')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category')),
                ('dietary_requirements', models.ManyToManyField(to='menu.DietaryRequirements')),
            ],
        ),
    ]