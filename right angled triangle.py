#code to print right angled triangle

rows = 5 # This line initializes a variable rows with the value 5. This variable represents the number of rows in the triangle.

for i in range(0, rows):
    for j in range(0, i+1):
        print('*', end = ' ') # This line prints an asterisk without moving to the next line.
                              #The end=' ' argument ensures that a space is printed after each asterisk.
    print("\r")

#After the inner loop completes for the current row, this line prints a newline character
#(\r is used for a carriage return). This moves the cursor to the beginning of the line for the next iteration of the
#outer loop, creating a new line for the next row.