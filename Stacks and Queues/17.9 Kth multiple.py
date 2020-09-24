
"""
Kth Multiple: Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7.
Note that 3, 5, and 7 do not have to be factors,but it should not have any other prime factors.
For example,the first several multiples would be(in order) 1,3,5,7,9,15, 21.
"""

"""
Will maintain 3 queues and multiply again and again
"""


def k_multiple(k):
    res_Q = [1, 3, 5, 7]
    temp_Q = [3, 5, 7]
    multiples = [3, 5, 7]

    if k <= 0:
        raise ValueError(" value can't be less than 1")
    if k < 5:
        return res_Q[k-1]

    while len(res_Q) < k:
        next_element = temp_Q.pop(0)

        for i in multiples:
            allow_element = next_element * i
            if allow_element not in res_Q:
                res_Q.append(allow_element)
                temp_Q.append(allow_element)

    return res_Q[-1]


print(k_multiple())


"""
Can do better
"""