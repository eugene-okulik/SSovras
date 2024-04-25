temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
warm_temperature = list(filter(lambda x: x > 28, temperatures))
print(f'The highest temp: {max(warm_temperature)}°C')
print(f'The lowest temp: {min(warm_temperature)}°C')
print(f'The average temp: {round((sum(warm_temperature)) / len(warm_temperature), 1)}°C')
