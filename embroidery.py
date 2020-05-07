# -------------------------------------------------------------------------------------------------
#                                            Embroidery
# -------------------------------------------------------------------------------------------------
#
#       The program is to design simple ornament matrices for Christmas fair. It creates a matrix
# where 0 means an empty pixel, and positive integers mean different colors.
#
# -------------------------------------------------------------------------------------------------


# ---------------------------------------- main functions -----------------------------------------

def draw_rectangle(width, height, border_color=1, fill_color=1, border_width=1):
    '''
    Creats the rectangle matrix like this:

        1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
        1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
        1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
        1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
        1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
        1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
    '''
    matrix = []
    for row_no in range(height):
        row = []
        for col_no in range(width):
            fill_pattern = border_color if any([
                                            row_no + 1 <= border_width,       # first row
                                            height - row_no <= border_width,  # last row
                                            col_no + 1 <= border_width,       # first column
                                            height - col_no <= border_width   # last column
                                            ]) else fill_color
            row.append(fill_pattern)
        matrix.append(row)

    return matrix


def draw_triangle(height, border_color=1, fill_color=1):
    '''
    Creats the rectangle matrix like this:

        0 0 0 1 0 0 0          0 0 0 1 0 0 0
        0 0 1 1 1 0 0          0 0 1 2 1 0 0
        0 1 1 1 1 1 0          0 1 2 2 2 1 0
        1 1 1 1 1 1 1          1 1 1 1 1 1 1
    '''
    width = 2 * height - 1
    return create_triangle(height, width, fill_color, border_color)


def draw_christmas_tree(blocks=4, border_color=1, fill_color=1):
    '''
    Creats the rectangle matrix like this:

        0 0 0 0 0 1 0 0 0 0 0
        0 0 0 0 1 2 1 0 0 0 0
        0 0 0 1 2 2 2 1 0 0 0
        0 0 0 0 1 2 1 0 0 0 0
        0 0 0 1 2 2 2 1 0 0 0
        0 0 1 2 2 2 2 2 1 0 0
        0 0 0 1 2 2 2 1 0 0 0
        0 0 1 2 2 2 2 2 1 0 0
        0 1 2 2 2 2 2 2 2 1 0
        0 0 1 2 2 2 2 2 1 0 0
        0 1 2 2 2 2 2 2 2 1 0
        1 1 1 1 1 1 1 1 1 1 1
    '''
    height = 3
    width = 11
    # width = 5 + (blocks - 1) * 2  # 5 - the base of the tree in the first block; 2 - distance between the bases of the trees of the next blocks

    matrix = []
    matrix = create_triangle(height, width, fill_color, border_color, border_last_row=False, base_width=7)

    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    '''Draws on screen (console) created the matrix with patterns.'''
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end=' ')
        print()
    print()


# -------------------------------------- internal functions ---------------------------------------

def create_triangle(matrix_height, matrix_width, fill_color, border_color, border_last_row=True, base_width=None):
    '''
    Returns matrix filled with triangle pattern. Default values: base_width = matrix_width

        0 0 0 1 0 0 0           0 0 0 1 0 0 0           0 0 0 0 0 1 0 0 0 0 0           0 0 0 1 2 2 2 1 0 0 0
        0 0 1 2 1 0 0           0 0 1 2 1 0 0           0 0 0 0 1 2 1 0 0 0 0           0 0 1 2 2 2 2 2 1 0 0
        0 1 2 2 2 1 0           0 1 2 2 2 1 0           0 0 0 1 2 2 2 1 0 0 0           0 1 2 2 2 2 2 2 2 1 0
        1 1 1 1 1 1 1           1 2 2 2 2 2 1

        height = 4              matrix_height = 4       matrix_height = None            matrix_height = None
        matrix_width = 7        matrix_width = 7        matrix_width = 11               matrix_width = 11
        base_width=None         base_width=None         base_width=7                    base_width=None
        border_last_row=True    border_last_row=False   border_last_row=True            border_last_row=False
    '''
    def fill_empty(matrix_height, matrix_width, base_width):
        '''Fills matrix with empty cells (zeros).'''
        matrix = []

        for row_no in range(matrix_height):
            empty_cell = matrix_height - 1 - row_no  # number of empty cells in half of the row
            row = []
            for col_no in range(matrix_width):
                row.append(0) if (col_no + 1 <= empty_cell or matrix_width - col_no <= empty_cell) else row.append("")  # empty cells from left or right side
            matrix.append(row)
        return matrix

    def fill_border(matrix, border_color):
        '''Fills matrix with border cells.'''
        height, width = len(matrix), len(matrix[0])

        for row_no in range(height):
            for col_no in range(width):
                if matrix[row_no][col_no] == "":  # cell to fill
                    if row_no + 1 == height:  # last row
                        if border_last_row:  # last row filled with border cells
                            matrix[row_no][col_no] = border_color
                        else:  # last row filled like middle row
                            if col_no + 1 == 1 or col_no + 1 == width:
                                matrix[row_no][col_no] = border_color
                            else:
                                matrix[row_no][col_no] = fill_color
                    else:  # middle row to fill
                        if matrix[row_no][col_no - 1] == 0 or matrix[row_no][col_no + 1] == 0:  # cell for empty or before empty cells
                            matrix[row_no][col_no] = border_color
        return matrix

    def fill_normal(matrix, fill_color):
        '''Fills matrix with normaln filled cells.'''
        height, width = len(matrix), len(matrix[0])

        for row_no in range(height):
            for col_no in range(width):
                if matrix[row_no][col_no] == "":  # cell to fill
                    matrix[row_no][col_no] = fill_color
        return matrix

    # ------- create_triangle main code -------
    if base_width is None:
        base_width = matrix_width

    matrix = fill_empty(matrix_height, matrix_width, base_width)
    matrix = fill_border(matrix, border_color)
    matrix = fill_normal(matrix, fill_color)

    return matrix


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    color_scheme = {0: '0', 1: '1', 2: '2', "": " "}

    print("Rectangle:")
    embroider(draw_rectangle(19, 19, 1, 2, 3), color_scheme)
    print("Triangle:")
    embroider(draw_triangle(10, border_color=1, fill_color=2), color_scheme)
    # print("Christmas tree:")
    # embroider(draw_christmas_tree(4), color_scheme)
