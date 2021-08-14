def gasoline_function():
    gasoline1 = float(input('enter gasoline gallon : '))
    one_litr = gasoline1 * 3.7854
    barel = gasoline1 * 1/19.5
    C02 = gasoline1 * 20 
    Etanol_gallon = gasoline1 * 115.000 / 75.700
    Dollar_price = gasoline1 * 4
    print('How many liters? -',one_litr)
    print('How many barrels? -',barel)
    print('What is the amount of CO2? -',C02)
    print('What is the energy value of a gallon of ethanol? -',Etanol_gallon)
    print('What is the price in dollars? -',Dollar_price)
gasoline_function()
