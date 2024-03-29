# Generated by Django 4.2 on 2024-01-23 10:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_value', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bases', to='currencies.currency')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currencies.currency')),
            ],
        ),
    ]
