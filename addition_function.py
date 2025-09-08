def addition():
        """Return the sum of 2 float values inputted by the user"""
        print('Return the sum of 2 float values. \n')
        # Loop for allowing user to re-input values if incorrect format at first
        while True: 
                num1 = input('Enter value 1 (must be float value): ')
                num2 = input('Enter value 2 (must be float value): ')
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    print(f'Calculating: {num1:f} + {num2:f}')
                    sum = num1 + num2
                    break
                except ValueError: 
                    print('Invalid data format, re-try with float')

        return sum

x = addition()
print('Sum = ', x)