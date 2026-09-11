import asyncio
import random
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbt9tRljzCs_IYaB7hclQ8ujS7PqHjRMsjSkddxOiRNN_LsmwGQMLF4w7tApcqnod1UiVLImJ_rZZ15JhpyUzZshbWS9bvE3c6A-PbYqykec4POAwrFUudEUFKTVZSCh0rt7c6EtO4mXUOfedXanATv_uZSn5Wx8kvzvRAm3l6607TgqzVdE7fg7VDE8LgRJGa0auyr8OgbXtCzlh7bBdR0bkwxwahVB8rAIZgeplDeXZlAUWZn1qJ0ifl5dypDbxoMjpGCwxrLaCSjyPin2dAQwUj-v93iGjRH3ujOHdQW31tJpGmLRnz3N4WSDW2_aBR9L-98hBWI9iIwoKI-mOKD8"

async def point_task(client, recipient):
    """Send dot‑messages every 60–70 seconds."""
    ma = alaf = naz = kar = tamiz = shird = shirf = gard = kiss = gaza = bare = alafyab = zebelgaza = 0

    while True:
        await asyncio.sleep(random.uniform(60, 70))
        
        ma += 1
        alaf += 1
        naz += 1
        kar += 1
        tamiz += 1
        shird += 1
        shirf += 1
        gard += 1
        kiss += 1
        gaza += 1
        bare += 1
        alafyab += 1
        zebelgaza += 1

        if ma >= 5:
            await client.send_message(recipient, 'مع')
            ma = 0
        if alaf >= 7:
            await client.send_message(recipient, 'علف')
            alaf = 0
        if gaza >= 35:
            await client.send_message(recipient, 'غذا بده همه')
            gaza = 0
        if naz >= 9:
            await client.send_message(recipient, 'نازش کن')
            naz = 0
        if tamiz >= 10:
            await client.send_message(recipient, 'تمیزش کن')
            tamiz = 0
        if shird >= 10:
            await client.send_message(recipient, 'شیر بز')
            shird = 0
        if gard >= 10:
            await client.send_message(recipient, 'گردش')
            gard = 0
        if kiss >= 10:
            await client.send_message(recipient, 'بوسش کن')
            kiss = 0
        if bare >= 15:
            await client.send_message(recipient, 'برداشت بز زبل')
            bare = 0
        if kar >= 15:
            await client.send_message(recipient, 'جمع آوری کارخانه')
            kar = 0
        if shirf >= 30:
            await client.send_message(recipient, 'فروش شیر')
            shirf = 0
        if alafyab >= 5:
            await client.send_message(recipient, 'خرید علف یاب')
            alafyab = 0
        if zebelgaza >= 5:
            await client.send_message(recipient, 'غذا بز زبل')
            zebelgaza = 0

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()
    recipient = "@BozPointEntegham"   # ⬅️ Replace with actual recipient
    await point_task(client, recipient)

if __name__ == '__main__':
    asyncio.run(main())
