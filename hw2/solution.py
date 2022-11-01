"""
1-> pass
2-> a,b,c
3-> d,e,f
4-> g,h,i
5-> j,k,l
6-> m,n,o
7-> p,q,r,s
8-> t,u,v
9-> w,x,y,z
0-> _ interval
-1 -> new char with the same num
"""


def get_letter(num,count):
    nums_chars = {-1: ('',),
                  1: ('',),
                  2: ('A', 'B', 'C'),
                  3: ('D', 'E', 'F'),
                  4: ('G', 'H', 'I'),
                  5: ('J', 'K', 'L'),
                  6: ('M', 'N', 'O'),
                  7: ('P', 'Q', 'R', 'S'),
                  8: ('T', 'U', 'V'),
                  9: ('W', 'X', 'Y', 'Z'),
                  0: (' ',)}
    while count >= len(nums_chars[num]):
        count -= len(nums_chars[num])
    return nums_chars[num][count]


def nums_to_text(nums):
    text = ""
    c = 0
    previous = 1
    for n in nums:
        if n == 1:  # we need to add the previous letter
            text += get_letter(previous, c)
            c = 0
        elif n == -1:
            # if c != 0:
            # print(f"We are on {n} and c={c}")
            text += get_letter(previous, c)
            # print(text)
            c = 0
        else:
            if previous == n:
                c += 1
                # print(f"We are on {n} and c={c}")
            else:
                text += get_letter(previous, c)
                # print(text)
                c = 0
        previous = n

    # if c != 0:
    text += get_letter(previous, c)
    # print(text)

    return text


def text_to_nums(text):
    nums = []
    return nums


def nums_to_angle(nums):
    angle = 0
    return angle


def angles_to_nums(angles):
    nums = []
    return nums


def is_phone_tastic(word):
    return 1
