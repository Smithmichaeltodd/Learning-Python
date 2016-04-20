#Whats The Temperature.py
#A Fahrenheit to Celsius Converter
#By Michael Smith

def temperature():
    print("Hi, I'm the temperature converter")
    C = eval(input("Please input the temperature in Celsius: "))
    F = (9/5)*C+32
    print("The temperature is", end=" ")
    print(F, end=" ")
    print("degrees Fahrenheit", end=" ")


temperature()
