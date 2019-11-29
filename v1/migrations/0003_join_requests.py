# Generated by Django 2.1.7 on 2019-11-29 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_teams_section_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join_Requests',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Users')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Teams')),
            ],
        ),
    ]
