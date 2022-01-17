# author: Lm(AMDG) 1/15/21
while True:
    temperature = float(input("Enter the temperature: "))
    scale = str.capitalize(input("Is it in Celcius(C) or is it in Farenheit(F)? "))

    try:
        if scale == "F":
            if temperature == 32:
               new_temp = 0
            else:
                new_temp = (temperature - 32) / 9
        elif scale == "C":
            new_temp = temperature / 5

    except TypeError:
        print("Invalid, enter a letter into the input.")
    except ValueError:
        print("Enter a number into the input")
    finally:
        try: 
            print(new_temp)
        finally:
            try_again = str.capitalize(input("Enter 'Y' if you want to try again or 'N' for no. "))
            if try_again == "N":
                break
