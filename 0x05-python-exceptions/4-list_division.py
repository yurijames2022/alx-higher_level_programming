#!/usr/bin/python3

# A function that divides element by element 2 lists

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            i += 1
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
            i += 1
            continue
        except TypeError:
            new_list.append(0)
            print("wrong type")
            i += 1
            continue
        except IndexError:
            new_list.append(0)
            print("out of range")
            break
        finally:
            pass
    return new_list
