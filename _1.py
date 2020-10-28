""" palindrome.py
Operators and Funtions Used: Slicing, Modulo Operator, len(), upper()
Logic: 1. Insert the string. Converted the string into capital. Calculate the
                length of the string. The length will either be an odd number or an
                even number.
            2. If even, divide by 2. If not, subtract 1 from the length number and
                then divide by 2.
            3. Calculated pairs of the string. Ignored the character that is falling in
                the center and has no character to pair with. Also, this character
                would not have any affect on the processing. The example is 'd' in the
                word 'Madam'. In this case we have two pairs: Mm, and aa. The
                character 'd' is common and can be ignored.
            4. Ran the loop as many times as the number of pairs.
            5. Compared each pair if both the characters are equal. Moved through
                the index from 0 position and -1 position.
            6. Displayed appropriate message and audio signal.
            7. Exit by pressing 'X' or 'x'
Referred for concept:
    https://www.youtube.com/watch?v=41QJN0TJqss
    https://www.youtube.com/watch?v=dCnxQGMpKz0
"""

from os import system
from datetime import datetime
import time
# import math
from intermediate_static_data import assignment_4, palindrome_hdg


symbol = '-'
border = (f'{symbol}') * 90
int_flag = 0


def cls_routine():

    time.sleep(2)  # Wait for 2 seconds before clearing the screen
    system('cls')  # Clear the screen


def interface():
    symbol = '-'
    spaces = ' '
    dsp_current_date = str()
    # border = (f'{symbol}') * 90
    print(f'{spaces}' * 90)
    print(border)
    print(f'|               {assignment_4:^60}             |')
    print('|                                                                           X to Quit    |')
    print(border)
    current_date = datetime.today()
    dsp_current_date = (current_date.strftime('%d-%m-%Y  %H:%M'))
    print(f'             {dsp_current_date:>75}')
    print(f' {spaces:<76} ')
    print()
    print(f'               {palindrome_hdg:^60}              ')
    print()


interface()


def is_palindrome():
    int_flag = 0
    word_length = int()
    while int_flag == 0:
        a = str(input('          Enter A String: '))  # User input
        b = a.upper()  # Converted string to UPPER case
        if b == 'X':
            print('Quit..')
            cls_routine()
            int_flag = 1
            # break
        else:
            word_length = len(b)  # Calculate the length of the string.
            print()
            print('          Text length...:', word_length)
            int_flag = 1
            # break

    if word_length % 2 == 0:  # Checking if the number of char is even
        total_pairs = word_length/2  # If true, ascertain the number of pairs.
#        pass
    else:
        word_length = word_length - 1  # if odd, subtract 1 and make it even
        total_pairs = word_length/2  # Ascertain the number of pairs.
    int_flag = 1
    # Run loop as many times as the number of pairs
    n = 0
    m = 0
    while n != int(total_pairs):
        if b[n] == b[m-1]:  # Compare the character at index 0 with the one at -1
            n = n + 1
            m = m - 1
            if n == total_pairs:  # Loop completion condition to display message
                print()
                print('          Palindrome')
                break
        else:
            print('\a')
            m = m - 1
            print('          Mismatch characters at position ', n, 'and', m)
            print()
            print('          Not a palindrome')
            break
    if b != 'X':
        print(border)


is_palindrome()
