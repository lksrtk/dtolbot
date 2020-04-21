#discord用
import discord
#line用
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

# 通知するDiscordチャンネル
DISCORD_CHANNEL_ID = 701877375394119790
# 通知するLINEチャンネル
LINE_CHANNEL_ID = 'C426f147441f3b5588de6f7212b3b1308'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
client = discord.Client()

# DiscordBOT起動時
@client.event
async def on_ready():
    print('ログインしました')

# Discordメッセージ受信時
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メッセージに"@LINE"が含まれなければ無視する
    if '@line' not in message.content:
        return

    # LINEに転送する
    try:
        line_bot_api.push_message(LINE_CHANNEL_ID, TextSendMessage(text=message.content))
        # 指定のdiscordチャンネルに返す
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        await channel.send("<次のメッセージがLINEに転送されました>\n"+message.content)
    except LineBotApiError as e:
        print(e)
        # 指定のdiscordチャンネルに返す
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        await channel.send("<LINEに転送出来ませんでした>\n"+e)

# Botの起動とDiscordサーバーへの接続
client.run(DISCORD_TOKEN)