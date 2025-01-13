import numpy as np

# A matrix operation tool for basic matrix operations
def operation(matrix1: np.ndarray, matrix2: np.ndarray, operation: str):
    try:
        if operation == '+':
            return np.add(matrix1, matrix2)
        elif operation == '-':
            return np.subtract(matrix1, matrix2)
        elif operation == '*':
            return np.dot(matrix1, matrix2)
        else:
            return "Invalid operation"
    except ValueError as e:
        return f"Error: {e}"

def get_matrix_input():
    """
    Helper function to parse matrix input from the user.
    """
    try:
        matrix = input("Enter your matrix (rows separated by ';' and values by ','): ")
        matrix = np.array([list(map(int, row.split(','))) for row in matrix.strip().split(';')])
        return matrix
    except ValueError:
        print("Invalid matrix format. Please ensure rows are separated by ';' and values by ',' (e.g., '1,2,3;4,5,6').")
        return None

if __name__ == "__main__":
    num_of_mat = int(input("How many matrices do you have for matrix operation? "))
    list_of_mat = []

    while num_of_mat > 0:
        matrix = get_matrix_input()
        if matrix is not None:
            list_of_mat.append(matrix)
            num_of_mat -= 1

    if len(list_of_mat) < 2:
        print("Need at least two matrices for the operation.")
    else:
        mat_operation = input("What kind of operation do you want to do (+, -, *): ").strip()
        result = list_of_mat[0]
        valid_operation = True

        for i in range(1, len(list_of_mat)):
            result = operation(result, list_of_mat[i], mat_operation)
            if isinstance(result, str):  # Error message returned from `operation`
                print(result)
                valid_operation = False
                break

        if valid_operation:
            print("Result of the operation:")
            print(result)

    print('Thanks for using this tool.')
