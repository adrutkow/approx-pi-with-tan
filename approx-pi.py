from math import tan


def approx_pi(step):
    """Function that takes as the parameter the desired amount of digits of pi
    calculated using tan"""
    my_pi = 0
    for i in range(0, step):
        highest = 0
        highest_index = 0
        for ii in range(0, 10):
            x = tan((my_pi + ii * 0.1 ** i) / 2)
            if x > highest:
                highest = x
                highest_index = ii
        my_pi = my_pi + highest_index * 0.1 ** i
    return my_pi


if __name__ == '__main__':
    print(approx_pi(16))
