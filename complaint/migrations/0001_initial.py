# Generated by Django 2.2.2 on 2020-03-31 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(default='', max_length=100)),
                ('complaint', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('replied', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(default='notreplied', max_length=20)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]