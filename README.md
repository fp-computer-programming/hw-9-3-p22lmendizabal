<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    HW 9-3
</h1>

<h2 align="center">Due before 8:30 AM on 1/19 (20 pts.)</h2>

### Try/Except Loops
---
Answer each of the following questions in a separate Python file named `hw9-3-#.py` where `#` is the number of the question. In your heading, put your name and the date you began working on the file.

1. Write a program to convert between celsius and farenheit. The program user should be asked to input a temperature and a temperature scale. Conversion : c/5 = f-32/9 (where c = temperature in celsius and f = temperature in fahrenheit). The program should be able to handle errors with either input by displaying a message to the user givingt he best prompts for acceptable input when the user tries again. Regardless of success with user input, the program should display a message to the user asking them to try converting again. (10 pts.)

2. Edit the following code to except for 2 different types of errors for user input. Each exception should display a specific message to help the user fix their mistake. Regardless of possible errors with input, a message should display thanking the user for using the program. (10 pts.)
    ```python
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
    ```

<p align="center">Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
