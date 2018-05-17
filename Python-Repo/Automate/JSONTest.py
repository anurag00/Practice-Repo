import requests, sys, logging, json, datetime, time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def timeConversion(time):
    t = datetime.datetime.fromtimestamp(time)
    # fmt = "%Y-%m-%d %H:%M:%S"
    fmt = "%H:%M:%S"
    return t.strftime(fmt)

def tempConversion(temp):
    #Celcius = Kalvin - 273.15
    return temp - 273.5

if __name__ == "__main__":
    # TODO: Reads the requested location from the command line.
    if len(sys.argv) > 1:
        location = ' '.join(sys.argv[1:]).title()
    else:
        print("Input the location(city) for the weather forcast => ",end='')
        location = input().title()
    logging.debug(location)

    # TODO: Check City Name in "G:\Pycode\Automate\city.list.json\city.list.json"
    jsonFile = open("G:\Pycode\Automate\city.list.json\city.list.json",'r',encoding="utf8")
    jsonText = jsonFile.read()
    pyText = json.loads(jsonText)
    city = []
    for x in pyText:
        if x['name'] == location:
            logging.debug("City ID = " + str(x['id']) + " Name = " + str(x['name']) + " Country = " + str(x['country']))
            city.append(x)
    if len(city) > 1:
        logging.debug("Found multiple cities with the same name")   # going with the first result in this caase
    elif len(city) < 1:
        logging.debug("No City found with the name " + location)
        exit("Not Found")
    else:
        logging.debug("City Found")
    logging.debug(city[0])

    # TODO: Downloads JSON weather data from OpenWeatherMap.org.
    APIFile = open(r'G:\Pycode\Automate\API\OpenWeatherApp.txt','r')
    APIKey = APIFile.readline()
    APIFile.close()
    logging.debug(APIKey)
    # api.openweathermap.org/data/2.5/weather?id=2172797&APPID=
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?id=" + str(city[0]['id']) + "&APPID=" + str(APIKey))
        res.raise_for_status()
    except Exception as ex:
        print("Error is Found : " + str(ex))
        print("Exiting...")
        exit()

    # Remove this later
    logging.debug(res.text)
    tempFile = open(r'G:/Anurag/WeatherLog.txt', 'w')
    tempFile.write(res.text)
    tempFile.close()

    # TODO: Converts the string of JSON data to a Python data structure.
    pyText = json.loads(res.text)

    # TODO: Print the weather forecast.
    dt = datetime.datetime.now()
    '''
    example JSON OUTPUT
    
    {'base': 'stations',
    'clouds': {'all': 40},
    'cod': 200,
    'coord': {'lat': 28.61, 'lon': 77.23},
    'dt': 1524225600,
    'id': 1261481,
    'main': {'humidity': 11,
             'pressure': 1002,
             'temp': 311.15,
             'temp_max': 311.15,
             'temp_min': 311.15},
    'name': 'New Delhi',
    'sys': {'country': 'IN',
            'id': 7809,
            'message': 0.0067,
            'sunrise': 1524183619,
            'sunset': 1524230397,
            'type': 1},
    'visibility': 3500,
    'weather': [{'description': 'dust', 'icon': '50d', 'id': 761, 'main': 'Dust'}],
    'wind': {'deg': 230, 'gust': 10.3, 'speed': 5.1}}
    '''

    print("{0}, {1}".format(pyText['name'],pyText['sys']['country']))
    print("Weather Report for " + str(dt.date()) + " ( " + str(timeConversion(time.time())) + " ) :\n")
    print("The weather will be {0}".format(pyText['weather'][0]['main']))
    print("The temperature will be {0:.2f} C  (Min : {1:.2f} C , Max : {2:.2f} C)".format(tempConversion(pyText['main']['temp']),
                                                                          tempConversion(pyText['main']['temp_min']),
                                                                          tempConversion(pyText['main']['temp_max'])))
    print("Humidity : {0}%".format(pyText['main']['humidity']))
    print("Wind Speed : {0}".format(pyText['wind']['speed']))
    print("Sunrise : {0}, Sunset : {1}".format(timeConversion(pyText['sys']['sunrise']),
                                               timeConversion(pyText['sys']['sunset'])))
    print("") #empty line