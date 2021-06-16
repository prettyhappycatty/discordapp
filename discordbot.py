# インストールした discord.py を読み込む
import discord
import random

# 設定全般まとめる
BOT_NAME = "cats0830v"
SERVER_NAME = "cattyのサーバー"
RAISE_WORD = "/random_teruteru"
RAISE_WORD_CONFIRM = "/who_is"
MSG_WORD = "てるてる"
WHO_IS_TARGET = ""

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'x'

# 接続に必要なオブジェクトを生成
#client = discord.Client()
intents = discord.Intents.default()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したらがDMが返る処理
    if message.content == RAISE_WORD:
        guild = discord.utils.get(client.guilds, name=SERVER_NAME)
        online_members = []
        #ステータスがオンラインのメンバーを取得
        for member in guild.members:
            if member.status == discord.Status.online and member:
                if member.name != BOT_NAME:#ほんとはBotじゃないという条件にしたい
                    online_members.append(member)
                    print(member.name, " is online")
        #メンバーのランダム一人とのDMを作る
        target_idx = random.randrange(len(online_members))
        #DMを送る
        for i in range(len(online_members)):
            dm_channel = await member[i].create_dm()
            if target_idx == i:
                WHO_IS_TARGET = member[i].name
                await dm_channel.send(MSG_WORD)
            else:
                await dm_channel.send("not " + MSG_WORD)
        print("完了")
    
    if message.content == RAISE_WORD_CONFIRM:
        await message.channel.send(WHO_IS_TARGET + " is " + MSG_WORD)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
