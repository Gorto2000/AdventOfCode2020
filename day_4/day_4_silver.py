# This function checks for one passport string if all fields
# are available. If one is missing, the function returns immediately
# zero. If the passport is correct, it returns 1. This is used in the
# main function to sum easily the number of correct passports.
def valid_passport(passport_string):
    expected_tokens = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for token in expected_tokens:
        if passport_string.count(token) == 0:
            return 0
    return 1

def main():
    current_passport = ""
    correct_passports = 0

    # The data of one passport can spread over several lines, so we
    # concatenate the passport data until there is an empty line -
    # there we can check whether the passport is correct.
    # At the end of the for-loop, we then check the last passport
    # from the input file.
    input_file = open("day_4_input.txt", "r")
    for line in input_file:
        if line == '\n':
            correct_passports += valid_passport(current_passport)
            current_passport = ""
        else:
            current_passport += line.rstrip('\n') + ' '
    else:
        correct_passports += valid_passport(current_passport)
        
    print("Result:", correct_passports)
    
if __name__ == '__main__':
    main()
