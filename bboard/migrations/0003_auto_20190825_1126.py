# Generated by Django 2.1.11 on 2019-08-25 11:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard', '0002_auto_20190823_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activated', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(error_messages={'invalid': 'Неправильное название товара! В названии должно быть от 4 до 50 символов'}, max_length=50, validators=[django.core.validators.RegexValidator(regex='^.{4,}$')], verbose_name='Товар'),
        ),
        migrations.AlterUniqueTogether(
            name='bb',
            unique_together={('title', 'published')},
        ),
    ]