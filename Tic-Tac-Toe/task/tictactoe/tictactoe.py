
def print_cells(lists):
    print("---------")
    for row in lists:
        print("|", end=" ")
        for elements in row:
            if elements == "_":
                print(" ", end=" ")
            elif elements == "X" or elements == "O":
                print(elements, end=" ")
        print("|")
    print("---------")


def check_x_wins(l_o_c):
    if l_o_c[0][0] == l_o_c[0][1] == l_o_c[0][2] == "X":
        return True
    elif l_o_c[1][0] == l_o_c[1][1] == l_o_c[1][2] == "X":
        return True
    elif l_o_c[2][0] == l_o_c[2][1] == l_o_c[2][2] == "X":
        return True
    elif l_o_c[0][0] == l_o_c[1][0] == l_o_c[2][0] == "X":
        return True
    elif l_o_c[0][1] == l_o_c[1][1] == l_o_c[2][1] == "X":
        return True
    elif l_o_c[0][2] == l_o_c[1][2] == l_o_c[2][2] == "X":
        return True
    elif l_o_c[0][0] == l_o_c[1][1] == l_o_c[2][2] == "X":
        return True
    elif l_o_c[0][2] == l_o_c[1][1] == l_o_c[2][0] == "X":
        return True


def check_o_wins(l_o_c):
    if l_o_c[0][0] == l_o_c[0][1] == l_o_c[0][2] == "O":
        return True
    elif l_o_c[1][0] == l_o_c[1][1] == l_o_c[1][2] == "O":
        return True
    elif l_o_c[2][0] == l_o_c[2][1] == l_o_c[2][2] == "O":
        return True
    elif l_o_c[0][0] == l_o_c[1][0] == l_o_c[2][0] == "O":
        return True
    elif l_o_c[0][1] == l_o_c[1][1] == l_o_c[2][1] == "O":
        return True
    elif l_o_c[0][2] == l_o_c[1][2] == l_o_c[2][2] == "O":
        return True
    elif l_o_c[0][0] == l_o_c[1][1] == l_o_c[2][2] == "O":
        return True
    elif l_o_c[0][2] == l_o_c[1][1] == l_o_c[2][0] == "O":
        return True


def check_for_winners(inp_string, cells_l):

    if check_o_wins(cells_l):
        print("O wins")
        return True
    elif check_x_wins(cells_l):
        print("X wins")
        return True
    elif check_o_wins(cells_l) is not True and check_x_wins(cells_l) is not True and inp_string.count("_") == 0 and c:
        print("Draw")
        return True



def main():
    cells = "_________"

    list_cells = list(cells)

    slice1 = list_cells[:3]
    slice2 = list_cells[3:6]
    slice3 = list_cells[6:9]
    list_of_cells = [slice1, slice2, slice3]
    print_cells(list_of_cells)
    count = 1
    while check_for_winners(cells, list_of_cells) is not True:
        cor_cord = False
        if count == 10:
            print("Draw")
            break
        while cor_cord is False:
            cordianates = input("Enter the coordinates:")
            if cordianates[0].isdigit() is False or cordianates[2].isdigit() is False:
                print("You should enter numbers!")
            elif int(cordianates[0]) > 3 or int(cordianates[2]) > 3 or int(cordianates[0]) < 1 or int(cordianates[2]) < 1:
                print("Coordinates should be from 1 to 3!")
            elif list_of_cells[int(cordianates[0]) - 1][int(cordianates[2]) - 1].isalpha():
                print("This cell is occupied! Choose another one!")
            else:
                row = int(cordianates[0]) - 1
                col = int(cordianates[2]) - 1
                if count % 2 == 1:
                    list_of_cells[row][col] = "X"
                else:
                    list_of_cells[row][col] = "O"
                count += 1
                print_cells(list_of_cells)

                cor_cord = True



main()