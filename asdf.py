import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("/채팅봇 도움말 ㄱㄱ")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/채팅봇 도움말"):
         await message.channel.send("`'/채팅봇 안녕'으로 인사 가능함.'/채팅봇 도움말'으로 도움말 알아볼수 있음'/채팅봇 제작자'로 채팅봇 제작자를 알 수 있음.`")
    if message.content.startswith("/채팅봇 안녕"):
         await message.channel.send("ㅎㅇ")
    if message.content.startswith("/채팅봇 제작자"):
         await message.channel.send("위대한 설빙 Snow ice 입니다")

client.run("NTc5MTg1ODQ0OTg5MTk4MzQ2.XN--zg.YkBcDx7xJxn3EcoAZKRTemjCle4")



