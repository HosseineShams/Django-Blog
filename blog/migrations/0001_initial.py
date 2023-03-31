# Generated by Django 4.1.7 on 2023-03-18 18:48

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('body', models.TextField(verbose_name='توضیحات')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('author', models.CharField(max_length=50, verbose_name='نویسنده')),
                ('tags', models.CharField(max_length=50, verbose_name='تگ ها')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts-images/', verbose_name='تصویر')),
                ('publish', models.BooleanField(default=True, verbose_name='انتشار')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]
