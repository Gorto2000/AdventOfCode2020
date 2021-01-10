def find_triple(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print("First number: ", numbers[i])
                    print("Second number: ", numbers[j])
                    print("Third number: ", numbers[k])
                    print("Result: ", numbers[i] * numbers[j] * numbers[k])
                    return

def main():
    numbers = []
    input_file = open("day_1_input.txt", "r")
    for line in input_file:
        number = int(line)
        numbers.append(number)

    find_triple(numbers)
    
if __name__ == '__main__':
    main()
