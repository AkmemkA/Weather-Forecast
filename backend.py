import requests

API_KEY = "1a223444ed3adcccd618a5d9c26de3a1"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&APPID={API_KEY}"
    number_of_observations = forecast_days * 8
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:number_of_observations]
    return filtered_data


if __name__ == "__main__":
    print(get_data('Moscow', 3, "Sky"))
