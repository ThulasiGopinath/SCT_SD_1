def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, from_scale, to_scale):
    if from_scale == 'C':
        if to_scale == 'F':
            return celsius_to_fahrenheit(value)
        elif to_scale == 'K':
            return celsius_to_kelvin(value)
    elif from_scale == 'F':
        if to_scale == 'C':
            return fahrenheit_to_celsius(value)
        elif to_scale == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_scale == 'K':
        if to_scale == 'C':
            return kelvin_to_celsius(value)
        elif to_scale == 'F':
            return kelvin_to_fahrenheit(value)
    else:
        raise ValueError("Invalid temperature scale.")

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    from_scale = input("Convert from (C, F, K): ").upper()
    to_scale = input("Convert to (C, F, K): ").upper()
    
    try:
        result = convert_temperature(value, from_scale, to_scale)
        print(f"{value}°{from_scale} = {result:.2f}°{to_scale}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
