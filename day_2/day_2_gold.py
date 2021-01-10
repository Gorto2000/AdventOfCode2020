import re 

# Task: Check if the password fits to the password rule
# in the same line. For this, each text line is splitted
# with a regular expression into its parts. The rule defines
# at which position the character from parsed_string[2] has
# to be in the password - but only in exactly one of the given
# two positions! Positions in the passwords have to be counted
# starting with 1, not with 0!
def main():
    correct_passwords = 0
    password_counter = 0
    
    input_file = open("day_2_input.txt", "r")
    for line in input_file:
        password_counter += 1
        char_found = 0

        parsed_string = re.split('\-|,| |\:', line)
        pos1 = int(parsed_string[0]) - 1
        pos2 = int(parsed_string[1]) - 1

        if parsed_string[4][pos1] == parsed_string[2]:
            char_found += 1
        if parsed_string[4][pos2] == parsed_string[2]:
            char_found += 1

        if char_found == 1:
            correct_passwords += 1

    print("Correct passwords: ", correct_passwords)
    print("Number of passwords: ", password_counter)
    
    
if __name__ == '__main__':
    main()
