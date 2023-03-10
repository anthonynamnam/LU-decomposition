import numpy as np


class Matrix:
    values = []
    determinant = None

    def __init__(self, n_row, n_col, all_zero=True, two_d_array=None):
        self.values = []
        self.n_row = n_row
        self.n_col = n_col
        if two_d_array is not None:
            assert type(two_d_array) == list and type(two_d_array[0]) == list
            n_row = max(len(two_d_array), n_row)
            n_col = max(max([len(row) for row in two_d_array]), n_col)
            for i in range(n_row):
                row_val = []
                for j in range(n_col):

                    try:
                        row_val.append(float(two_d_array[i][j]))
                    except:
                        row_val.append(0)
                self.values.append(row_val)
        elif all_zero:
            for i in range(n_col):
                row_val = []
                for j in range(n_row):
                    row_val.append(0.0)
                self.values.append(row_val)

        self.calculate_determinant()

    def calculate_determinant(self):
        self.determinant = np.linalg.det(np.array(self.values))

    def print_shape(self):
        print(f"Matrix Shape: ({self.n_col},{self.n_row})")

    def print_values(self, matrix_name=""):
        if len(matrix_name) > 0:
            print(f"{matrix_name}:")
        for row in self.values:
            for row_val in row:
                print(f"{row_val}\t", end="")
            print("")
        print("")

    def set_diagonal(self, values=1):
        assert self.n_col == self.n_row, "set_diagonal only available to square matrix"
        for i in range(self.n_col):
            self.values[i][i] = values


def LU(M: Matrix, print_step=False) -> tuple():
    # Check if the martix is square matrix
    assert M.n_col == M.n_row, "This matrix is not a square matrix"
    assert M.determinant != 0, "Determinant of this matrix = 0"

    for i in range(M.n_col):
        # Assign diagonal value
        M.values[i][i] = M.values[i][i]

        # Step a
        for j in range(i + 1, M.n_col):
            M.values[j][i] = M.values[j][i] / M.values[i][i]
            M.values[i][j] = M.values[i][j]

        if print_step:
            print(f"After Iteration {i+1}a:")
            M.print_values()

        # Step b
        for j in range(i + 1, M.n_col):
            for k in range(i + 1, M.n_row):
                M.values[j][k] -= M.values[j][i] * M.values[i][k]

        if print_step:
            print(f"After Iteration {i+1}b:")
            M.print_values()

    # Split it into L and U
    L = Matrix(M.n_row, M.n_col)
    L.set_diagonal()

    U = Matrix(M.n_row, M.n_col)

    for i in range(M.n_row):
        for j in range(M.n_col):
            if i <= j:
                U.values[i][j] = M.values[i][j]
            else:
                L.values[i][j] = M.values[i][j]

    return (L, U)
