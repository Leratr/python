"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""

from bs4 import BeatifulSoup
import requests
import lxml

page = requests.get("https://sochi.technopark.ru/smartfony/")
import requests

cookies = {
    'qrator_ssid': '1680077780.957.VDCyGnJWpfqylRPL-tr1ucgq17iqfqerf0ndgm2cq54qnfhqa',
    'stest201': '0',
    'stest207': 'acc1',
    'stest209': 'ct2',
    'PHPSESSID': '695e72af1ecfc654298a138786632a5e',
    'user_public_id': 'Lxh46hrM3nnmajFS6w6aTT5CaAwaCLNRkZnAtqo6SdrbE05%2BszgqaXQxrXCQqNLI',
    '_gcl_au': '1.1.1471040737.1680077786',
    '_gid': 'GA1.2.444682417.1680077786',
    '_ym_uid': '1680077786631282479',
    '_ym_d': '1680077786',
    'tmr_lvid': '4678e9dc68936b4c65339441f8d6954f',
    'tmr_lvidTS': '1680077786240',
    '_ym_visorc': 'w',
    'adrdel': '1',
    'adrcid': 'AQ670Jd_ol-UQ5Rilb7xHWQ',
    'afUserId': '4de438a5-34ee-484d-a22c-e16cbed43006-p',
    'AF_SYNC': '1680077799863',
    '_ym_isad': '1',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    '_userGUID': '0:lfteyp2a:AhKlIpBOVTRIIGvE2E0M5faS9EgdmWAI',
    'dSesn': 'b1730682-9a20-23de-95ff-4cbca6dba465',
    '_dvs': '0:lfteyp2a:lKlj1hHhanYqAheXK7fAJB8bn7VpXgxY',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20346a0756e425ef67140a%22}',
    'tp_city_id': '38733',
    'pageviewTimer': '40.038',
    'qrator_jsid': '1680077783.114.r5SIFZnqi2dry0Di-a015n6s9ohf39npi50l0knutl0ln9ell',
    'visitedPagesNumber': '5',
    '_ga_RD4H4CBNJ3': 'GS1.1.1680077786.1.1.1680078164.56.0.0',
    'tmr_detect': '0%7C1680078166753',
    'mindboxDeviceUUID': 'e69c39f7-9912-431a-bd79-1119abc2f7a8',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22e69c39f7-9912-431a-bd79-1119abc2f7a8%22%7D',
    'promo1000closed': 'true',
    '_ga': 'GA1.2.1864189232.1680077786',
    'pageviewTimer': '829.6469999999999',
}

headers = {
    'authority': 'sochi.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'qrator_ssid=1680077780.957.VDCyGnJWpfqylRPL-tr1ucgq17iqfqerf0ndgm2cq54qnfhqa; stest201=0; stest207=acc1; stest209=ct2; PHPSESSID=695e72af1ecfc654298a138786632a5e; user_public_id=Lxh46hrM3nnmajFS6w6aTT5CaAwaCLNRkZnAtqo6SdrbE05%2BszgqaXQxrXCQqNLI; _gcl_au=1.1.1471040737.1680077786; _gid=GA1.2.444682417.1680077786; _ym_uid=1680077786631282479; _ym_d=1680077786; tmr_lvid=4678e9dc68936b4c65339441f8d6954f; tmr_lvidTS=1680077786240; _ym_visorc=w; adrdel=1; adrcid=AQ670Jd_ol-UQ5Rilb7xHWQ; afUserId=4de438a5-34ee-484d-a22c-e16cbed43006-p; AF_SYNC=1680077799863; _ym_isad=1; pageviewTimerFired15=true; pageviewTimerFired30=true; _userGUID=0:lfteyp2a:AhKlIpBOVTRIIGvE2E0M5faS9EgdmWAI; dSesn=b1730682-9a20-23de-95ff-4cbca6dba465; _dvs=0:lfteyp2a:lKlj1hHhanYqAheXK7fAJB8bn7VpXgxY; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20346a0756e425ef67140a%22}; tp_city_id=38733; pageviewTimer=40.038; qrator_jsid=1680077783.114.r5SIFZnqi2dry0Di-a015n6s9ohf39npi50l0knutl0ln9ell; visitedPagesNumber=5; _ga_RD4H4CBNJ3=GS1.1.1680077786.1.1.1680078164.56.0.0; tmr_detect=0%7C1680078166753; mindboxDeviceUUID=e69c39f7-9912-431a-bd79-1119abc2f7a8; directCrm-session=%7B%22deviceGuid%22%3A%22e69c39f7-9912-431a-bd79-1119abc2f7a8%22%7D; promo1000closed=true; _ga=GA1.2.1864189232.1680077786; pageviewTimer=829.6469999999999',
    'if-none-match': '"144453-8X1ucS6h2NmZo+pmrU0JXGSC2pA"',
    'referer': 'https://sochi.technopark.ru/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers)
with open("technopark.html", "0", enconding = "UTF-8") as f:
    f.write(response.text)