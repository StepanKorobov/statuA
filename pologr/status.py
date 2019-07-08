from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import data
import datetime
import time
login, password = data.LoginAndData()
vk_session = vk_api.VkApi(token="ab9917efbfc2bb8c383d3ef6b32afcc33d5b103b734f1072a6d63be92e6bcd29bfe07d25516650fa8a702")

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    delta = datetime.timedelta(hours=3, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)

    new = datetime.datetime.now()

    newYear = datetime.datetime(2020, 1, 1, 0, 0, 0)

    NewYearDay = newYear - new
    NewYearHour = round(NewYearDay.seconds / 3600)
    NewYearHourRP = round(NewYearDay.seconds / 3600, 1)

    if NewYearHour > NewYearHourRP:
        NewH = str((NewYearHour)-1)
    else:
        NewH = str(NewYearHour)

    yui = t.hour
    if yui >= 10 and yui <= 16:
        imgpic = "🌝"
        print(yui)
    elif yui == 22 or yui == 23 or yui == 0 or yui == 1 or yui == 2:
        imgpic = "🌚"
        print(yui)
    elif yui == 20 or yui == 21 or yui == 3:
        imgpic = "🌙"
        print(yui)
    elif yui >= 5 and yui <= 9 or yui >= 17 and yui <= 19:
        imgpic = "💦"
        print(yui)
    else:
        imgpic = "🐳"
        print(yui)

    NewD = str(NewYearDay.days)

    print(NewYearDay.days)
    print(NewYearHour)
    print(NewYearHourRP)

    nowtime = t.strftime("%H:%M:%S")
    nowdate = t.strftime("%d.%m.%y")

    on = vk_session.method("friends.getOnline")
    counted = len(on)

    vk_session.method("status.set", {"text":imgpic + nowtime + "●" + nowdate + "●" + "🏳‍🌈Гей на " + str(counted) + "0%" + " До Мировой дрочки  " + NewD + " Дней " + NewH + " Часов"})

    time.sleep(30)