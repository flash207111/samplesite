# Generated by Django 2.1.11 on 2019-08-25 11:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('bboard', '0001_initial'), ('bboard', '0002_auto_20190823_0839'), ('bboard', '0003_auto_20190825_1126')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Товар')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['-published'],
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Rubric', verbose_name='Рубрика'),
        ),
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
