def temperature():
    air_temp = float(input('enter the air temp : '))
    air_speed = float(input('enter the air speed : '))
    wct_index = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    print('Index : ',wct_index,)
temperature()