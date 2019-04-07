import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("Bot is Online!")
    print(client.user.name)
    print(client.user.id)
    print("--------------")
    await client.change_presence(game=discord.Game(name='"/워드봇 도움" 입력 ㄱㄱ', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("/워드봇 도움"):
        await client.send_message(message.channel, "\n``도움`` : 모든 도움은 '워드봇'으로 시작합니다. (아닌 것은 다른 문구가 붙습니다.) \n\n``주사위`` : 'ㅈ 도움'을 입력하세요 \n\n``동전던지기`` : 'ㄷ 도움'을 입력하세요 \n\n``W!정보`` : 자신의 디코 가입날짜, 아이디, 현 디코 프사를 보실 수 있습니다. \n\n``인사, 놀자, 죽어, 꺼져 등...`` : 워드가 일침 아닌 일침을 날릴 겁니다. \n\n``W!뭐 할까? / W!골라`` : 이 명령어를 치면 워드가 랜덤으로 아무 말이나 해줄 겁니다. \n(예 : W!골라 콜라 사이다 \n\n제작 서버 링크 : **https://discord.gg/8UG9nkK** \n개발자 문의 : 박재영#9400")

    if message.content.startswith("워드봇 안녕"):
        await client.send_message(message.channel, "안녕하세요. 쿼트의 리메이크, 워드봇 입니다.")

    if message.content.startswith("워드봇 인사"):
        await client.send_message(message.channel, "안 사")

    if message.content.startswith("ㅈ 도움"):
        await client.send_message(message.channel, "d 양 옆에 숫자는 아무거나 써주시면 되지만 너무 큰 숫자는 인식하지 못합니다.\n명령어 : 주사위 3d6")

    if message.content.startswith("ㄷ 도움"):
        await client.send_message(message.channel, "말 그대로 동전던지기 입니다. 확률은 50 : 50 입니다 \n명령어 : 동전던지기")

    if message.content.startswith("ㅅ 도움"):
        await client.send_message(message.channel, "심심할 때 팀 나누는 용도로 쓰실 수 있습니다. \n예시 명령어 : W!팀 나누기 1 2 3 4/5 6 7 8")        
       

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
