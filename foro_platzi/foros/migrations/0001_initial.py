# Generated by Django 4.1.7 on 2023-02-21 21:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('thematic', models.CharField(blank=True, max_length=24, null=True)),
                ('post_text', models.TextField(default=None, max_length=1000)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_profile.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now_add=True)),
                ('text_comment', models.TextField(max_length=500)),
                ('original_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foros.commentmodel')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.postmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_profile.usersmodel')),
            ],
        ),
    ]
