def main():
    numbers = []
    
    input_file = open("day_1_input.txt", "r")
    for line in input_file:
        number = int(line)
        numbers.append(number)

    # Task: Look for two entries in numbers that can be summed up
    # to "2020". This task can be done by looping through all entries
    # in the list and by looking if the difference to "2020" is also in
    # the list.
    for number in numbers:
        searched_number = 2020 - number
        if searched_number in numbers:
            print("First number: ", number)
            print("Second number: ", searched_number)
            print("Result: ", number * searched_number)
            break
    
if __name__ == '__main__':
    main()
