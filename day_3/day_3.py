# For day 3, the silver and gold task could be done with the same
# implementation.

def main():
    # Coordinate system:
    # -> x
    # |
    # v
    # y

    # Slopes are input as well (silver task is slope (3, 1):
    slopes_x = [1, 3, 5, 7, 1]
    slopes_y = [1, 1, 1, 1, 2]

    topo = []
    input_file = open("day_3_input.txt", "r")
    for line in input_file:
        topo.append(line)

    result = 1
    for i in range(5):

        pos_x = 0
        pos_y = 0
        tree_counter = 0

        while pos_y < len(topo):
            # Since the topographical pattern repeats itself to
            # the right, we can use the modulo operation on the
            # x position to stay in the input file data
            if topo[pos_y][pos_x % 31] == '#':
                tree_counter += 1
            
            pos_x += slopes_x[i]
            pos_y += slopes_y[i]

        print("Slope", str(i + 1), ":", tree_counter)
        result *= tree_counter

    print("Result:", result)
    
if __name__ == '__main__':
    main()
