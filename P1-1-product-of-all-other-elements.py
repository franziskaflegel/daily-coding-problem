# Problem 1.1

import numpy as np


def product_of_all_other_elements(mylist):
    result_list = [0]*len(mylist)
    for i in range(0, len(mylist)):
        result_list[i] = int(np.prod(mylist[:i])*np.prod(mylist[i+1:]))
    return result_list


test_list = [1, 0, 3]

print(product_of_all_other_elements(test_list))
