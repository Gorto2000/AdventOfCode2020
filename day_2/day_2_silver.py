import re 

# Task: Check if the password fits to the password rule
# in the same line. For this, each text line is splitted
# with a regular expression into its parts. The rule defines
# how often the character in parsed_string[2] has to be in the
# password (lower and upper limit).
def main():
    correct_passwords = 0
    password_counter = 0
    
    input_file = open("day_2_input.txt", "r")
    for line in input_file:
        password_counter += 1

        parsed_string = re.split(r"\-|,| |\:", line)
        lower_limit = int(parsed_string[0])
        upper_limit = int(parsed_string[1])
        count = parsed_string[4].count(parsed_string[2])
        if count >= lower_limit and count <= upper_limit:
            correct_passwords += 1

    print("Correct passwords: ", correct_passwords)
    print("Number of passwords: ", password_counter)
    
    
if __name__ == '__main__':
    main()
