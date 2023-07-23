import requests

#API ключ от WeatherApi
api_key="#вставьте сюда свой ключ.Получить его можно по ссылке:www.weatherapi.com/signup.aspx"
#даём пользователю выбор
weather= input('''
1.Москва
2.Рязань
3.Санкт-Петербург
4.Саранск
какую погоду вы хотите узнать?:''')
#переводим полученное число в целое число
weather = int(weather)

if weather==1:
            #делаем запрос Api
            url = f'http://api.weatherapi.com/v1/current.json?lang=ru&key={api_key}&q=Moscow'
            response = requests.get(url)
            data = response.json()
            # Извлекаем данные о температуре и описании погоды
            temp = data["current"]["temp_c"]
            weather2 = data["current"]["condition"]["text"]
            weather3 = data["current"]["feelslike_c"]
            weather4 = data["current"]["last_updated"]


            # Выводим информацию о погоде
            print(f"текущая температура в Москве ({temp}°C)")
            print(f"за окном {weather2}")
            print(f"ощущается как {weather3} ")
            print(f"последнее обновление данных о погоде {weather4}")


else:
    pass

if weather==2:
            #делаем запрос Api
            url = f'http://api.weatherapi.com/v1/current.json?lang=ru&key={api_key}&q=Ryazan'
            response = requests.get(url)
            data = response.json()
            # Извлекаем данные о температуре и описании погоды
            temp = data["current"]["temp_c"]
            weather2 = data["current"]["condition"]["text"]
            weather3 = data["current"]["feelslike_c"]
            weather4 = data["current"]["last_updated"]

            # Выводим информацию о погоде
            print(f"текущая температура в Рязани ({temp}°C)")
            print(f"за окном {weather2}")
            print(f"ощущается как {weather3} ")
            print(f"последнее обновление данных о погоде {weather4}")

else:
    pass

if weather==3:

    url = f'http://api.weatherapi.com/v1/current.json?lang=ru&key={api_key}&q=Sankt-Peterburg'
    response = requests.get(url)
    data = response.json()
    # Извлекаем данные о температуре и описании погоды
    temp = data["current"]["temp_c"]
    weather2 = data["current"]["condition"]["text"]
    weather3 = data["current"]["feelslike_c"]
    weather4 = data["current"]["last_updated"]

    # Выводим информацию о погоде
    print(f"текущая температура в Санкт-Петербурге ({temp}°C)")
    print(f"за окном {weather2}")
    print(f"ощущается как {weather3} ")
    print(f"последнее обновление данных о погоде {weather4}")

else:
    pass

if weather==4:

    url =  f'http://api.weatherapi.com/v1/current.json?lang=ru&key={api_key}&q=Saransk'
    response = requests.get(url)
    data = response.json()
    # Извлекаем данные о температуре и описании погоды
    temp = data["current"]["temp_c"]
    weather2 = data["current"]["condition"]["text"]
    weather3 = data["current"]["feelslike_c"]
    weather4 = data["current"]["last_updated"]

    # Выводим информацию о погоде
    print(f"текущая температура в Саранске ({temp}°C)")
    print(f"за окном {weather2}")
    print(f"ощущается как {weather3} ")
    print(f"последнее обновление данных о погоде {weather4}")


else:
    pass

#если пользователь выбирает число которого нет в списке,мы выводим ошибку
if weather >=5:
    print("не правильный выбор")
else:
    pass
#Ожидание нажатия клавиши Enter для продолжения
input("Нажмите Enter для продолжения...")

