import requests

API_KEY = "1a223444ed3adcccd618a5d9c26de3a1"


def get_data(place, forecast_days=None, data_to_display=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&APPID={API_KEY}"
    number_of_observations = forecast_days * 8
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:number_of_observations]
    if data_to_display == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if data_to_display == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data('Moscow', 3, "Sky"))
