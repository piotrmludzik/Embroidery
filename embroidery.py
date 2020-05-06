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
    matrix = []
    # fill_pattern = None

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


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
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


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    color_scheme = {0: '~', 1: '1', 2: '2'}
    # embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)

    embroider(draw_rectangle(6, 6, 1, 2, 2), color_scheme)
