def convert_to_snafu(decimal_nbr: int):
    """
     Decimal          SNAFU
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       11             21
       12             22
       13             1== (25 * 1 + -2 * 5 + -2)
       14             1=- (25 * 1 + -2 * 5 + -2)
       15             1=0 (25 * 1 + -2 * 5 + 0)
       16             1=1 (25 * 1 + -2 * 5 + 1)
       17             1=2 (25 * 1 + -2 * 5 + 2)
       18             1-= (25 * 1 + -1 * 5 + -2)
       19             1-- (25 * 1 + -1 * 5 + -1)
       20             1-0 (25 * 1 + -1 * 5 + 0)
       21             1-1 (25 * 1 + -1 * 5 + 1)
       22             1-2 (25 * 1 + -1 * 5 + 2)
       23             10=  (25 * 1 + 0 * 5 + -2)
       24             10- (25 * 1 + 0 * 5 + -1)
       25             100 (25 * 1 + 0 * 5 + 0)
       26             101 (25 + 0 + 1)
       27             101 (25 + 0 + 2)
       28             11= (25 + 5 + -2)
       29             11- (25 + 5 + -1)
       30             110 (25 + 5 + 0)
       31             111 (25 + 5 + 1)
       32             112 (25 + 5 + 2)
       33             12= (25 + 10 + -2)
       34             12- (25 + 10 + -1)
       35             120 (25 + 10 + 0)
       62             222 (2*25 + 2*5 + 2)
       63             1=== (125 - 50 - 10 -2)
       312            2222 (2*125 + 2*25 + 2*5 + 2)
       313            1=== (125 - 50 - 10 - 2)
       1562           22222 (625*2 - 125*2 + 25*2 + 5*2 + 2)
       1563           1===== (3125*1 - 625*2 - 125*2 - 25*2 - 5*2 - 2)
       7812           222222 (3125*2 + 625*2 + 125*2 + 25*2 + 5*2 + 2)
       7813           1====== (15625 - 3125*2 - 625*2 - 125*2 - 25*2 - 5*2 - 2)
     2022             1=11-2
    12345             1-0---0
314159265  1121-1110-1=0
    :param decimal_nbr:
    :return:


    extra digit after
    2, 12, 62. 312, 1562, 7812
    2, 10, 50, 250, 1250, 6250
    digits
    1  2   3   4    5     6
    1-2
    3-12,
    13-62
    63-312
    313-1562
    1563-7812

https://science.widener.edu/~schultz/mathhelp2.html
math.log(math.pow(5,3), 5)
    3, 13, 63, 313, 1563, 7812
    2, 10, 50, 250, 1250, 6250,
    5- based
    Fist how many digits,
    2 -> 2
    1 -> 1
    0 -> 0
    - -> -1
    = -> -2

    1-based
    10,100,1000,1000

    """
    pass


def length_of_snafu(decimal_nbr: int):
    """
    extra digit after:
    2, 12, 62. 312, 1562, 7812
    increment 5 base
    2, 10, 50, 250, 1250, 6250
    number of snafu
    1,  2,  3,   4,    5,    6
    :param decimal_nbr: based-10 number
    :return: length of the snafu number / string
    """
    base_int, length, increment = 2, 1, 10
    while decimal_nbr > base_int:
        length += 1
        base_int += increment
        increment *= 5
    return length


def convert_to_snafu(decimal_nbr: int):
    snafu_length = length_of_snafu(decimal_nbr)
    snafu = "1" if True else "2"
