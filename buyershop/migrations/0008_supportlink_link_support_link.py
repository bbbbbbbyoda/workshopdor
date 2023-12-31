# Generated by Django 4.1.7 on 2023-06-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyershop', '0007_remove_link_logo_link_social_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_link', models.URLField(max_length=500, verbose_name='Ссылка')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Поддержка',
                'verbose_name_plural': 'Поддержка',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='support_link',
            field=models.URLField(default=1, max_length=500, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
