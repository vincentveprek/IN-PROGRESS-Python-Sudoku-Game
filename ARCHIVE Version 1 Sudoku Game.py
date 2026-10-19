max_number = 81
max_on_line = 9
number_counter = 1

while number_counter <= max_number:
    counting = number_counter  # 1 2 3...81
    counting = counting - 1 # 0 1 2...80
    counting = counting % 3 # 0 1 2 0 1 2...2
    counting = counting + 1 # 1 2 3 1 2 3...3

    if (number_counter >= 10 and number_counter < 19 or
        number_counter >= 37 and number_counter < 46 or
        number_counter >= 64 and number_counter < 73): 
    
        counting = counting + 3

    if (number_counter >= 19 and number_counter < 28 or
        number_counter >= 46 and number_counter < 55 or
        number_counter >= 73 and number_counter < 82): 

        counting = counting + 6
        
    print(counting, end=' ')

#    if number_counter <= 8: # Line 1 to 9 horizontal number alignment.
#        print(end=' ')

    if number_counter % 3 == 0: # Formating horizontal spacing for every 3 numbers
       print(end='  ')    
        
    if number_counter % max_on_line == 0: # Formating for the vertical every 3 number spacing.
       print("")

    if number_counter / 9 % 3 == 0: # Final step creating 9*3 grid and making a space for the next 9*3
       print("")
        
    number_counter +=1
