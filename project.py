import re
import sys

def main():
    print("Welcome to the conversion system between the Metric system and the Anglo-Saxon system.")
    print('If you want to exit the program, enter "exit" at any time')
    convert = input('What would you like to convert, temperature, length, weight or volume ? ')

    while True:
        convert = convert.lower().casefold().strip()
        if convert == 'exit':
            sys.exit
            break
        if convert == "temperature" or convert == "length" or convert == "weight" or convert == "volume":
            break
        convert = input('Only accept "temperature", "length", "weight" or "volume". What would you like to convert ? ')

    if convert == "temperature":
        unidad = (input("Write the temperature you would like to convert (example: 33º F): "))
        while True:
            temp(unidad.casefold().strip())
            if unidad == 'exit':
                sys.exit
                break
            unidad = input("The data to be converted has not been entered correctly, try to put it as in the example (33º F or 33º C) ")

    elif convert == "weight":
        unidad = (input("What weight would you like to convert? (put with only two decimal, example: 40.23 lb): "))
        while True:
            weight(unidad.casefold().strip())
            if unidad == 'exit':
                sys.exit
                break
            unidad = input("The data to be converted has not been entered correctly, try to put it as in the example (40.23 kg) ")

    elif convert == "length":
        unidad = (input("What length would you like to convert? (put with only two decimal, example: 22.15 mi): "))
        while True:
            longitud(unidad.casefold().strip())
            if unidad == 'exit':
                sys.exit
                break
            unidad = input("The data to be converted has not been entered correctly, try to put it as in the example (40 mi) ")

    elif convert == "volume":
        unidad = (input("What length would you like to convert? (put with only two decimal, example: 22.15 gal): "))
        while True:
            volumen(unidad.casefold().strip())
            if unidad == 'exit':
                sys.exit
                break
            unidad = input("The data to be converted has not been entered correctly, try to put it as in the example (40 dl) ")


def temp(temp):
    # Celsius a Fahrenheit:  (Valor °C × 9/5) + 32
    # Fahrenheit a Celsius: (Valor °F − 32) × 5/9
    if matches := re.match(r"([+-]?\d+)º? ?(c|C|f|F)$", temp):
        if matches.group(2) == "c" or matches.group(2) == "C":
            sys.exit(print(f"{((int(matches.group(1)) * 9/5) + 32):.1f}º F"))
        else:
            sys.exit(print(f"{((int(matches.group(1)) - 32) * 5/9):.1f}º C"))


def weight(weight):
    # 1 g = 0.00220462 lb
    # 1 g = 0.035274 oz
    if matches := re.match(r"(\d+(\.\d+)?) ?(lb|pounds?|oz|ounces|g|grams?|kg|kilograms?)$", weight):
        if "kg" in matches.group(3) or "kilograms" in matches.group(3) or "g" in matches.group(3) or "grams" in matches.group(3):
            if matches.group(3) == "kg" or matches.group(3) == "kilograms":
                result = float(matches.group(1)) * 2.20462
            elif matches.group(3) == "g" or matches.group(3) == "grams":
                result = float(matches.group(1)) * 0.00220462
            sys.exit(print(f"{result:.2f} lb"))
        else:
            if matches.group(3) == "lb" or matches.group(3) == "pounds":
                result = float(matches.group(1)) * 0.453592
            elif matches.group(3) == "oz" or matches.group(3) == "ounces":
                result = float(matches.group(1)) * 0.0283495
            sys.exit(print(f"{result:.2f} kg"))


def longitud(long):
    # 1 in = 2.54 cm
    # 1 ft = 30.48 cm
    # 1 yd = 0.9144 m
    # 1 mi = 1.60934 km
    if matches := re.match(r"(\d+(\.\d+)?) ?(in|inche?s?|ft|feet|yd|yard|mi|miles?|mm|milimeter|dm|decimeter|cm|centimeter|m|meters?|km|kilometers?)$", long):
        if matches.group(3) in ["in", "inch", "inches"]:
            result = float(matches.group(1)) * 2.54
            sys.exit(print(f"{result:.2f} cm"))
        elif matches.group(3) in ["ft", "feet"]:
            result = float(matches.group(1)) * 30.48
            sys.exit(print(f"{result:.2f} cm"))
        elif matches.group(3) in ["yd", "yard"]:
            result = float(matches.group(1)) * 0.9144
            sys.exit(print(f"{result:.2f} m"))
        elif matches.group(3) in ["mi", "miles"]:
            result = float(matches.group(1)) * 1.60934
            sys.exit(print(f"{result:.2f} km"))
        elif matches.group(3) in ["mm", "milimeter"]:
            result = float(matches.group(1)) * 0.03937
            sys.exit(print(f"{result:.2f} in"))
        elif matches.group(3) in ["cm", "centimeter"]:
            result = float(matches.group(1)) * 0.3937
            sys.exit(print(f"{result:.2f} in"))
        elif matches.group(3) in ["dm", "decimeter"]:
            result = float(matches.group(1)) * 3.937
            sys.exit(print(f"{result:.2f} in"))
        elif matches.group(3) in ["m", "meters"]:
            result = float(matches.group(1)) * 1.0936
            sys.exit(print(f"{result:.2f} yd"))
        elif matches.group(3) in ["km", "kilometers"]:
            result = float(matches.group(1)) * 0.6214
            sys.exit(print(f"{result:.2f} mi"))


def volumen(capa):
    # 1 galon|gal = 3.78541 l
    # 1 quart|qt = 0.946353 l
    # 1 pint|pt = 47.3176 cl
    # 1 cup = 24 cl
    # 1 fluid ounce|fl oz = 2.95735 cl
    if matches := re.match(r"(\d+(\.\d+)?) ?(gal|gallon|qt|quart|pt|pint|cup|fl oz|fluid ounce|cl|centiliters?|l|liters?|ml|mililiters?|dl|deciliters?)$", capa):
        if matches.group(3) in ["gal", "gallon", "qt", "quart"]:
            if matches.group(3) in ["gal", "gallon"]:
                result = float(matches.group(1)) * 4
            elif matches.group(3) in ["qt", "quart"]:
                result = float(matches.group(1))
            sys.exit(print(f"{(result * 0.946353):.2f} l"))
        elif matches.group(3) in ["pt", "pint", "cup", "fl oz", "fluid ounce"]:
            if matches.group(3) in ["pt", "pint"]:
                result = float(matches.group(1)) * 16
            elif matches.group(3) == "cup":
                result = float(matches.group(1)) * 8
            elif matches.group(3) in ["fl oz", "fluid ounce"]:
                result = float(matches.group(1))
            sys.exit(print(f"{(result * 2.95735):.2f} cl"))
        elif matches.group(3) in ["cl", "centiliter", "centiliters", "ml", "mililiter", "mililiters", "dl", "deciliter", "deciliters"]:
            if matches.group(3) in ["ml", "mililiter", "mililiters"]:
                result = float(matches.group(1)) / 10
            elif matches.group(3) in ["dl", "deciliter", "deciliters"]:
                result = float(matches.group(1)) * 10
            elif matches.group(3) in ["cl", "centiliter", "centiliters"]:
                result = float(matches.group(1))
            sys.exit(print(f"{(result * 0.338):.2f} fl oz"))
        elif matches.group(3) in ["l", "liter", "liters"]:
            result = float(matches.group(1)) * 0.264172
            sys.exit(print(f"{result:.2f} gal"))


if __name__ == "__main__":
    main()
