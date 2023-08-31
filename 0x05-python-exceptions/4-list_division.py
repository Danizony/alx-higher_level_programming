#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.
    Args:
        my_list_1 (list): First list
        my_list_2 (list): Second list
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for x in range(0, list_length):
        try:
            division = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            divison = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return (new_list)
