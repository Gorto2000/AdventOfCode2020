import re

# This function checks for one passport string if all fields
# are available and if the field content is correct. If one is
# missing, the function returns immediately zero. If the passport
# is correct, it returns 1. This is used in the main function
# to sum easily the number of correct passports.
def valid_passport(passport_string):
    expected_tokens = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    output = []
    
    passport_fields = passport_string.split()
    for token in expected_tokens:
        token_found = False
        for field in passport_fields:
            if field.startswith(token):
                field_value = field.split(":")[1]
                output.append(field_value)
                if token == "byr" and int(field_value) >= 1920 and int(field_value) <= 2002:
                    token_found = True
                if token == "iyr" and int(field_value) >= 2010 and int(field_value) <= 2020:
                    token_found = True
                if token == "eyr" and int(field_value) >= 2020 and int(field_value) <= 2030:
                    token_found = True
                if token == "hgt":
                    if field_value.endswith("cm"):
                        field_value = field_value.split("cm")[0]
                        if int(field_value) >= 150 and int(field_value) <= 193:
                            token_found = True
                    if field_value.endswith("in"):
                        field_value = field_value.split("in")[0]
                        if int(field_value) >= 59 and int(field_value) <= 76:
                            token_found = True
                if token == "hcl" and re.match("#[0-9a-f]{6}", field_value) and len(field_value) == 7:
                    token_found = True
                if token == "ecl" and eye_colors.count(field_value) == 1:
                    token_found = True
                if token == "pid" and re.match("[0-9]{9}", field_value) and len(field_value) == 9:
                    token_found = True                            
                    
        if token_found == False:
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
        
    print(correct_passports)
    
if __name__ == '__main__':
    main()
