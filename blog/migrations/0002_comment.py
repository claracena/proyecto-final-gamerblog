# Generated by Django 4.0.5 on 2022-06-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
