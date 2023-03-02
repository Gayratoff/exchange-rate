from pyrogram import Client, filters, types,enums
import requests
import xml.etree.ElementTree as ET

api_id = 9797655 #API_ID : https://my.telegram.org/
api_hash = "5bab03171ae5e0d92ixx0ce70137943c" #API_HASH : https://my.telegram.org/
app = Client("KingsOfPy", api_id, api_hash,parse_mode=enums.parse_mode.ParseMode.HTML)



async def rubl_to_uzs(pul):
    po = 0
    response = requests.get("http://cbu.uz/uzc/arkhiv-kursov-valyut/xml/")
    xml = response.content
    m = ET.fromstring(xml)
    for val in m:
        if val.find('Ccy').text == f'{pul}':
            po = float(val.find('Rate').text)
    p =po
    tg_pul = 1 * p
    return tg_pul




@app.on_message(filters.command(commands='x',prefixes='.'))
async def hello(client, message):
    money = ['JPY', 'RUB', 'USD','EUR']
    pul = []
    for x in money:
        pul.append(await rubl_to_uzs(x))
    await app.edit_message_text(
          chat_id=message.chat.id,
          message_id=message.id,
          text=f"<b>1 EURO💶  - {pul[0]} So'm\n</b>"  
               f"<b>1 JPY💴 - {pul[0]} So'm\n</b>"
               f"<b>1 RUB💴 - {pul[1]} So'm\n</b>"
               f"<b>1 USD💵 - {pul[2]} So'm\n</b>"


     )


# Asosiy ishlash bo'limi.
app.run()
