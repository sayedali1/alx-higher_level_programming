#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrix_list in matrix:  # walk through each list
        # walk through each element in the list
        for index, i in enumerate(matrix_list, 1):
            # dlim between nums
            if index == len(matrix_list):
                space = ""
            else:
                space = " "
            print("{}".format(i), end=space)
        print("")
