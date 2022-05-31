import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = "https://api.telegram.org/bot"+token+"/sendMessage"
        a = text.find('{')
        b = text.find('}')
        c = text.rfind('{')
        d = text.rfind('}')
        if a and b and c and d:
            p1 = text[0:a]
            p2 = text[b+1:c]
            p3 = text[d:-1]

            text_slice = p1+ tg_name+p2+tg_phone+p3
        else:
            text_slice = text

        try:
            req = requests.post(api, data={
                'chat_id':chat_id,
                'text':text_slice
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Error")
            elif req.status_code == 500:
                print("Server Error")
            else:
                print("Success")

    else:
        pass