# Generated by Django 3.2.5 on 2021-07-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='type',
            field=models.CharField(blank=True, choices=[('A.공지사항', 'A.공지사항'), ('B.세소식', 'B.세소식'), ('C.기타', 'C.기타')], max_length=20, null=True),
        ),
    ]
