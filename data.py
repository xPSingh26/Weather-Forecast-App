import requests
API_KEY = "ad36f14edd61e0461007b431e4d7ef15"


def get_data(place, forecast_days=None, data_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    request = requests.get(url)
    data = request.json()
    filteredData = data['list']
    nrValue = forecast_days * 8
    filteredData = filteredData[:nrValue]
    return filteredData


if __name__ == "__main__":
    data = get_data('Jammu', 3, 'Temperature')
    print(data)

