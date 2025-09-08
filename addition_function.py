## ATMS 523 Assignment 1
## Created by Domenic Brooks

def addition():
        """Return the sum of 2 float values inputted by the user"""        
        print('\nReturn the sum of 2 float values.')
        # Loop for allowing user to re-input values
        # if incorrect format at first.
        while True: 
                num1 = input('Enter value 1 (must be float value): ')
                num2 = input('Enter value 2 (must be float value): ')
                # Try adding the two values, 
                # raise exception if formats are not floats.
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    print(f'Calculating: {num1} + {num2}')
                    sum = num1 + num2
                    # End loop if no exception raised
                    break 
                except ValueError: 
                    print('Invalid data format, re-try with float')

        return sum

# Run function and print results
x = addition()
print(f'Sum = {x:f}')