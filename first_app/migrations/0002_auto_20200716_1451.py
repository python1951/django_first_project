# Generated by Django 3.0.3 on 2020-07-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(default='social media', max_length=256, unique=True),
            preserve_default=False,
        ),
    ]
