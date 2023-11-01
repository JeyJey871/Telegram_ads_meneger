# Generated by Django 4.2.6 on 2023-11-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting_ads', '0002_alter_channel_config_from_channel_and_more'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='ready',
        ),
        migrations.CreateModel(
            name='Message_sent_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sent_status', models.BooleanField(default=False)),
                ('from_channel', models.ForeignKey(blank=True, limit_choices_to={'my_channel': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_channel', to='setting_ads.channels')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_sent_status', to='client.message')),
                ('to_channel', models.ForeignKey(blank=True, limit_choices_to={'my_channel': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_channel', to='setting_ads.channels')),
            ],
            options={
                'verbose_name_plural': 'message_sent_status',
                'db_table': 'message_sent_status',
            },
        ),
    ]
