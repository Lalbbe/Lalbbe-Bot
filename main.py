import discord
import datetime

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzQ5MTc4OTc4MTA2OTk4Nzg1.X0oNSw.8T6C8SKTn_bX-3yTc_2p-DmKR-4"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('제대일'):
        channel = message.channel
        await channel.send('2022년 3월 23일 금방 이제??')
    if message.content.startswith('쁘랄아 안녕'):
        channel = message.channel
        await channel.send('마 안녕 못하다 짜슥아 살려줘라.....')
    if message.content.startswith('연락두절 기간'):
        channel = message.channel
        await channel.send('논산 4주, 경찰 학교 3주 총 7주.....보고싶어도 참아 금방연락하마')
    if message.content.startswith('쁘랄이 정보'):
        channel = message.channel
        await channel.send('나이 21에 성별은 남자 하는일 의경이라지')
    if message.content.startswith('쁘랄이 번호'):
        channel = message.channel
        await channel.send('010-ㅁㅁㅁㅁ-ㅁㅁㅁㅁ 알사람은 알아서 알겠지뭐')
    if message.content.startswith('쁘랄이 뭐해'):
        channel = message.channel
        await channel.send('방패 들고 깝친다 뭐 어쩔래')
    if message.content.startswith('쁘랄아 놀자'):
        channel = message.channel
        await channel.send('나도 놀고 싶다.... 외출일때 와줘 놀자 밥사줄게')
    if message.content.startswith('쁘랄이 바보'):
        channel = message.channel
        await channel.send('어휴 누가봐도 정말순이겠구만 절래절래 다음은 빛나인가?')
    if message.content.startswith('쁘랄이 멍청이'):
        channel = message.channel
        await channel.send('이거또한 정말순이겠구만 으휴')
    if message.content.startswith('인편 쓰는법'):
        channel = message.channel
        await channel.send('```1. 폰에서 "더 캠프"를 다운받는다.'
                           '2. 다운후 가입을 하고 보고싶은 군인을 등록을 한다.'
                           '3. 성분: 병사'
                           ', 군종: 육군'
                           ', 이름: 나태훈'
                           ', 생년월일: 2000년 8월 14일'
                           ', 입영부대: 육군훈련소-논산'
                           ', 입대일자: 2020년 9월 24일'
                           ', 관계: 알맞게 설정'
                           '4. 카페 가입하기'
                           '5. 위문편지 누르고 편지 작성하기! 편지는 800자 넘기지 마시구 이상한 사진보내면 편지 못쓰게 하니까 찾아가서 죽어ㅎㅎ```')
    if message.content.startswith('!설명'):
        channel = message.channel
        await channel.send('```제대일, 남은 날짜, 연락두절 기간, 쁘랄아 안녕, 쁘랄이 정보, 쁘랄이 번호, 쁘랄이 뭐해, 쁘랄아 놀자, 쁘랄이 바보, 쁘랄이 멍청이, 인편 쓰는법```')
    if message.content.startswith('남은 날짜'):
      a = datetime.datetime(2022, 3, 23)
    b = datetime.datetime.now()
    c = (a-b)
    await message.channel.send(c일)



client.run(token)
