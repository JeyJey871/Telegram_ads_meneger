from django.contrib import admin
from .models import Client_Settings, Bot, Channels, KeywordChannelAds, Channel_config
# Register your models here.

admin.site.register(Client_Settings)
@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('id', 'bot_name', 'bot_token', 'bot_link', 'created_at', 'updated_at')


#inline for channels vs KeywordChannelAds

class KeywordChannelAdsInline(admin.TabularInline):
    model = KeywordChannelAds
    extra = 2


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel_name', 'channel_link', 'channel_id', 'my_channel', 'created_at', 'updated_at')
    inlines = [KeywordChannelAdsInline]
@admin.register(KeywordChannelAds)
class KeywordChannelAdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'channel', 'created_at', 'updated_at')



@admin.register(Channel_config)
class ChannelConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'from_channel', 'to_channel', 'bot', 'created_at', 'updated_at')