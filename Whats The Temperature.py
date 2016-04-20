#Whats The Temperature.py
#A Fahrenheit to Celsius Conveter
#By Michael Smith

def temperature():
    print("Hi, I'm the temperature converter")
    C = eval(input("Please input the temperature in Celsius: "))
    F = (9/5)*C+32
    print("The temperature is",F,"degrees Fahrenheit outside")

temperature()