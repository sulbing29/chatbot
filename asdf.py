import discord
import os

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
         await message.channel.send("`/채팅봇 안녕 /채팅봇 도움말 /채팅봇 제작자 /채팅봇 ? /채팅봇 채팅청소 /채팅봇 니얼굴 /채팅봇 뒤져"
                                    " /채팅봇 니얼굴못생김 /채팅봇 니가뭔데 /채팅봇 꺼져 /채팅봇 닥쳐`")
    if message.content.startswith("/채팅봇 안녕"):
         await message.channel.send("ㅎㅇ")
    if message.content.startswith("/채팅봇 제작자"):
         await message.channel.send("위대한 설빙 Snow ice 입니다")
    if message.content.startswith("/채팅봇 ?"):
         await message.channel.send("왜요?")
    if message.content.startswith("/채팅봇 채팅청소"):
         await message.channel.send("*지원되지 않는 형식입니다.*")
    if message.content.startswith("/채팅봇 니얼굴"):
         await message.channel.send("뒤져 ^-^")
    if message.content.startswith("/채팅봇 뒤져"):
        await message.channel.send("(하찮음) 쯧쯧")
    if message.content.startswith("/채팅봇 니얼굴못생김"):
        await message.channel.send("~~ㅇㅈ~~ 아니 뭔소리하는거지")
    if message.content.startswith("/채팅봇 니가뭔데"):
        await message.channel.send("~~사람인데~~ 아니 봇인데")
    if message.content.startswith("/채팅봇 닥쳐"):
        await message.channel.send("닥쳐? ㅇㅇ")
    if message.content.startswith("/진짜 채팅봇"):
        await message.channel.send("왜요")
    if message.content.startswith("/봇 공지"):
        await message.channel.send("@here 채팅봇 베타를 초대해 주셔서 정말 감사합니다. 저희는 아직 만든지 1일도 안되서 수많은 명령어가 생기면"
                                   "서 **봇이 실행이 안될 수** 있는 **오류가 발생할수 있습니다.** 이점 주의해 주시고"
                                   "잘 사용해주세요!")
         
        
access_token = os.inviron["BOT_TOKEN"]
client.run(access_token)



