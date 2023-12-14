""" Przykładowy moduł w jezyku Python test 2 """

__licznik = 0


def sum_lst(input_list):
    global __licznik
    __licznik += 1
    sum_list = 0
    for element in input_list:
        sum_list += element
    return sum_list


def unique_list(input_list):
    global __licznik
    __licznik += 1
    out_list = set(input_list)
    return list(out_list)


def unique_list_2(input_list):
    global __licznik
    __licznik += 1
    out_list = []
    for ele in input_list:
        if ele not in out_list:
            out_list.append(ele)
    return sorted(out_list)


if __name__ == "__main__":
    print("Wysołanie bezpośrednie(nie jako moduł)")
