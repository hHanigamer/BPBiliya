import os
import asyncio
import random
import logging
from splusthon import SoroushClient
from splusthon.sessions import StringSession

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SS = os.environ.get("SESSION_STRING")
if not SS:
    raise ValueError("متغیر محیطی SESSION_STRING در گیت‌هاب تنظیم نشده است!")

async def send_safe(client, recipient, message):
    try:
        await client.send_message(recipient, message)
        logging.info(f"پیام ارسال شد: {message}")
    except Exception as e:
        logging.error(f"خطا در ارسال '{message}': {e}")

async def point_task(client, recipient):
    logging.info("شروع تسک ارسال پیام‌ها...")
    naz = kar = tamiz = shird = shirf = gard = kiss = gaza = bare = alafyab = zebelgaza = legendary = 0
    while True:
        try:
            await asyncio.sleep(random.uniform(60, 70))
            naz += 1; kar += 1; tamiz += 1; shird += 1; shirf += 1; gard += 1
            kiss += 1; gaza += 1; bare += 1; alafyab += 1; zebelgaza += 1; legendary += 1
            
            if gaza >= 35: await send_safe(client, recipient, 'غذا بده همه'); gaza = 0
            if naz >= 9: await send_safe(client, recipient, 'نازش کن'); naz = 0
            if tamiz >= 10: await send_safe(client, recipient, 'تمیزش کن'); tamiz = 0
            if shird >= 10: await send_safe(client, recipient, 'شیر بز'); shird = 0
            if gard >= 10: await send_safe(client, recipient, 'گردش'); gard = 0
            if kiss >= 10: await send_safe(client, recipient, 'بوسش کن'); kiss = 0
            if bare >= 15: await send_safe(client, recipient, 'برداشت بز زبل'); bare = 0
            if kar >= 15: await send_safe(client, recipient, 'جمع آوری کارخانه'); kar = 0
            if shirf >= 30: await send_safe(client, recipient, 'فروش شیر'); shirf = 0
            if alafyab >= 5: await send_safe(client, recipient, 'علف یاب بخر'); alafyab = 0
            if legendary >= 30: await send_safe(client, recipient, 'خرید علف legendary'); legendary = 0
            if zebelgaza >= 30: await send_safe(client, recipient, 'غذا بز زبل'); zebelgaza = 0
        except Exception as e:
            logging.error(f"خطای غیرمنتظره: {e}")
            await asyncio.sleep(10)

async def main():
    logging.info("در حال راه‌اندازی کلاینت...")
    client = SoroushClient(StringSession(SS))
    try:
        await client.start()
        logging.info("کلاینت متصل شد.")
        recipient = "@BetaBoz"
        await point_task(client, recipient)
    except Exception as e:
        logging.critical(f"خطای بحرانی: {e}")
    finally:
        await client.disconnect()   # ← اصلاح شد
        logging.info("کلاینت متوقف شد.")

if __name__ == '__main__':
    asyncio.run(main())
