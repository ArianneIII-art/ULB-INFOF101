def gagnant(grille: list[list[str]]):
    colors = ["R", "J"]

    # for the column
    current_color_column = ["", "", "", "", "", "", ""]
    number_of_color_column = [0, 0, 0, 0, 0, 0, 0]

    # for the row
    for i in grille:
        current_color_ligne = ""
        number_of_color_ligne = 0

        for j in range(len(i)):
            # LIGNE #
            if i[j] == current_color_ligne:
                number_of_color_ligne += 1
            elif i[j] in colors:
                current_color_ligne = i[j]
                number_of_color_ligne = 1
            else:
                current_color_ligne = ""
                number_of_color_ligne = 0

            if number_of_color_ligne >= 4:
                print("line")
                return current_color_ligne

            # COLUMN #
            if i[j] == current_color_column[j]:
                number_of_color_column[j] += 1
            elif i[j] in colors:
                current_color_column[j] = i[j]
                number_of_color_column[j] = 1
            else:
                current_color_column[j] = ""
                number_of_color_column[j] = 0

            if number_of_color_column[j] >= 4:
                print("column")
                return current_color_column[j]

    # DIAGONALS
    rows = len(grille)
    columns = len(grille[0])
    nbr_of_digonal = rows + columns

    for i in range(1, nbr_of_digonal):
        current_color_column = ""
        number_of_color_column = 0

        y = max(0, i - rows)
        n_in_diagonal = min(i, rows, columns, nbr_of_digonal - i)

        x = min(i - 1, rows - 1)

        for _ in range(n_in_diagonal):
            if grille[x][y] == current_color_column:
                number_of_color_column += 1
            elif grille[x][y] in colors:
                current_color_column = grille[x][y]
                number_of_color_column = 1
            else:
                current_color_column = ""
                number_of_color_column = 0

            if number_of_color_column >= 4:
                print("diago")
                return current_color_column

            x -= 1
            y += 1

        current_color_column = ""
        number_of_color_column = 0
        y = max(0, i - rows)
        x = rows - min(i - 1, rows - 1) - 1

        for _ in range(n_in_diagonal):
            if grille[x][y] == current_color_column:
                number_of_color_column += 1
            elif grille[x][y] in colors:
                current_color_column = grille[x][y]
                number_of_color_column = 1
            else:
                current_color_column = ""
                number_of_color_column = 0

            if number_of_color_column >= 4:
                print("diago")
                return current_color_column

            x += 1
            y += 1


    # if no winner is found
    return None

"""print(
    f"ligne {gagnant([['J', 'J', 'J', 'J', 'V', 'V', 'V'],
                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                      ['V', 'V', 'V', 'V', 'V', 'V', 'V']])}",

    f"column {gagnant([['R', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['R', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['R', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['R', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                       ['V', 'V', 'V', 'V', 'V', 'V', 'V']])}",

    f"diagoniale {gagnant([['R', 'V', 'V', 'V', 'V', 'V', 'V'],     # 1
                           ['V', 'R', 'V', 'V', 'V', 'V', 'V'],     # 2
                           ['V', 'V', 'R', 'V', 'V', 'V', 'V'],     # 3
                           ['V', 'V', 'V', 'R', 'V', 'V', 'V'],     # 4
                           ['V', 'V', 'V', 'V', 'V', 'V', 'V'],     # 5
                           ['V', 'V', 'V', 'V', 'V', 'V', 'V']])}", # 6
                        #         7    8    9    10   11   12

    f"diagoniale {gagnant([['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                           ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                           ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
                           ['V', 'V', 'R', 'V', 'V', 'V', 'V'],
                           ['V', 'R', 'V', 'V', 'V', 'V', 'V'],
                           ['R', 'V', 'V', 'V', 'V', 'V', 'V']])}",

    f"None {gagnant([['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']])}",


sep="\n")"""

print(
gagnant([
    ['J', 'R', 'J', 'J', 'J', 'R', 'R'], 
    ['V', 'R', 'R', 'J', 'R', 'J', 'J'], 
    ['V', 'V', 'R', 'V', 'J', 'V', 'V'], 
    ['V', 'V', 'R', 'V', 'J', 'V', 'V'], 
    ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
    ['V', 'V', 'V', 'V', 'V', 'V', 'V']
  ])
)