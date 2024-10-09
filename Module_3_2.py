def send_email (message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email ("message", "vasyok1337@gmail.com")
send_email ("message", 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email ("message", 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email ("message", 'urban.teacher@mail.uk', sender='urban.student@mail.ru')
send_email ("message", 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



