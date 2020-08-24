import vk_api
import random
import time
token = "14ab5dd2960b0b74ba47a091c71f50e25f8d303061b0194928872be52d66e28a8012c371a9f7a373e3194"


vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    #главный цикл
    messages = vk.method ("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "привет":
            vk.method("messages.send", {"peer_id": id, "message": "хай !", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "хай":
             vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "как дела":
            vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "что делаешь":
            vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "норм":
            vk.method("messages.send", {"peer_id": id, "message":  "сколько тебе лет ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "хорошо":
            vk.method("messages.send", {"peer_id": id, "message":  "сколько тебе лет ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "тоже хорошо":
            vk.method("messages.send", {"peer_id": id, "message":  "сколько тебе лет ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "5":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "6":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "7":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "8":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "9":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "10":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "11":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "12":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "13":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "14":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "15":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "16":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "17":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "18":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "19":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "20":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "21":
            vk.method("messages.send", {"peer_id": id, "message":  "а мне 100000", "random_id": random.randint(1, 2147483647)})

        else:
            vk.method("messages.send", {"peer_id": id, "message":  "Я тебя непонял", "random_id": random.randint(1, 2147483647)})

    time.sleep(1)
