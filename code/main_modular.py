asu_metro = {
    "January": "Summer",
    "February": "Summer",
    "March": "Autumn",
    "April": "Autumn",
    "May": "Autumn",
    "June": "Winter",
    "July": "Winter",
    "August": "Winter",
    "September": "Spring",
    "October": "Spring",
    "November": "Spring",
    "December": "Summer"
}

asu_noon = {
    "January": "Birak",
    "February": "Bunuru",
    "March": "Bunuru",
    "April": "Djeran",
    "May": "Djeran",
    "June": "Makuru",
    "July": "Makuru",
    "August": "Dijiba",
    "September": "Dijiba",
    "October": "Kambarang",
    "November": "Kambarang",
    "December": "Birak"
}

spain_japan = {
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
    "September": "Autumn",
    "October": "Autumn",
    "November": "Autumn",
    "December": "Winter"
}

mauritius = {
    "January": "Summer",
    "February": "Summer",
    "March": "Summer",
    "April": "Summer",
    "May": "Autumn",
    "June": "Winter",
    "July": "Winter",
    "August": "Winter",
    "September": "Winter",
    "October": "Spring",
    "November": "Summer",
    "December": "Summer"
}


sri_mal = {
    "January": "Northeast Monsoon",
    "February": "Northeast Monsoon",
    "March": "Inter-Monsoon",
    "April": "Inter-Monsoon",
    "May": "Southeast Monsoon",
    "June": "Southeast Monsoon",
    "July": "Southeast Monsoon",
    "August": "Southeast Monsoon",
    "September": "Southeast Monsoon",
    "October": "Inter-Monsoon",
    "November": "Inter-Monsoon",
    "December": "Northeast Monsoon"
}
season_map = {
    "Australia": {
        "Metrological": asu_metro,
        "Noongar": asu_noon
    },
    "Spain": spain_japan,
    "Japan": spain_japan,
    "Mauritius": mauritius,
    "Sri lanka": sri_mal,
    "Malaysia": sri_mal
}

def get_month_weather_map(country, season=None):
    data = season_map.get(country)
    if season:
        data = data.get(season)
    return data

def get_weather(month_weather_map, month):
    return month_weather_map.get(month)

def get_weather_photo(weather):
    photo_map = {
        "Winter": "",
        "Spring": "",
        "Summer": "",
        "Autumn": "",
        "Northeast Monsoon": "",
        "Inter-Monsoon": "",
        "Southeast Monsoon": "",
        "Birak": "",
        "Bunuru": "",
        "Dijiba": "",
        "Djeran": "",
        "Makuru": "",
        "Kambarang": ""
    }
    return photo_map.get(weather)

if __name__ == "__main__":
    country, season, month = None, None, None

    print(f'Enter Country Name ({"|".join(season_map.keys())}):')
    country = input()
    if country not in season_map.keys():
        print(f'Please enter one of ({"|".join(season_map.keys())})')
        exit(0)
    if country == "Australia":
        print(f'Enter Season ({"|".join(season_map.get("Australia").keys())}):')
        season = input()
        if season not in season_map.get("Australia").keys():
            print(f'Please enter one of ({"|".join(season_map.get("Australia").keys())}):')
            exit(0)
            
    month_weather_map = get_month_weather_map(country, season)
    print(f'Enter Month ({"|".join(month_weather_map.keys())}):')
    month = input()
    if month not in month_weather_map.keys():
        print(f'Please enter one of ({"|".join(month_weather_map.keys())})')
        exit(0)

    weather = get_weather(month_weather_map, month)
    photo = get_weather_photo(weather)

    print(weather, photo)
