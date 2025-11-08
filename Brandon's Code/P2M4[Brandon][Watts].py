# [] create The Weather
file_name = "city_weather.txt"

with open(file_name, 'w') as weather_file:
    weather_file.write("Beijing,30.9\n")
    weather_file.write("Cairo,34.7\n")
    weather_file.write("London,23.5\n")
    weather_file.write("Nairobi,26.3\n")
    weather_file.write("New York City,28.9\n")

with open(file_name, 'a') as weather_file:
    weather_file.write("Sydney,26.5\n")
    weather_file.write("Tokyo,30.8\n")
    weather_file.write("Rio De Janeiro,30.0\n")

with open(file_name, 'r') as weather_file:
    print("[Brandon Watts]")

    line = weather_file.readline()
    while line:
        parts = line.strip().split(',')
        city = parts[0]
        temperature = parts[1]

        print(f"City of {city} month ave: highest high is {temperature} Celsius")

        line = weather_file.readline()

mean_temps = open("mean_temps.txt", 'a+')

mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")

mean_temps.seek(0)

headings = mean_temps.readline()

headings_list = headings.split(',')

city_temp = mean_temps.readline()

while city_temp:
    city_data = city_temp.split(',')
    
    print(f"City of {city_data[0]} month ave: highest high is {city_data[2].strip()} Celsius")
    
    city_temp = mean_temps.readline()

mean_temps.close()