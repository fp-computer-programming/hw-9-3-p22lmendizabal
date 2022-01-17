# author: LM (AMDG) 1/17/22
try:
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print("Enter a number.")
except ZeroDivisionError:
    print("The value in 'Previous' cannot be 0.")
finally:
    print("Thankyou for usig the program.")