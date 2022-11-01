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


def get_letter(num, count):
    nums_chars = {-1: ('',),
                  1: ('',),
                  0: (' ',),
                  2: ('A', 'B', 'C'),
                  3: ('D', 'E', 'F'),
                  4: ('G', 'H', 'I'),
                  5: ('J', 'K', 'L'),
                  6: ('M', 'N', 'O'),
                  7: ('P', 'Q', 'R', 'S'),
                  8: ('T', 'U', 'V'),
                  9: ('W', 'X', 'Y', 'Z')
                  }
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
    char_nums = {'': (1,),
                 ' ': (0,),
                 'A': (2,),
                 'B': (2, 2),
                 'C': (2, 2, 2),
                 'D': (3,),
                 'E': (3, 3),
                 'F': (3, 3, 3),
                 'G': (4,),
                 'H': (4, 4),
                 'I': (4, 4, 4),
                 'J': (5,),
                 'K': (5, 5),
                 'L': (5, 5, 5),
                 'M': (6,),
                 'N': (6, 6),
                 'O': (6, 6, 6),
                 'P': (7,),
                 'Q': (7, 7),
                 'R': (7, 7, 7),
                 'S': (7, 7, 7, 7),
                 'T': (8,),
                 'U': (8, 8),
                 'V': (8, 8, 8),
                 'W': (9,),
                 'X': (9, 9),
                 'Y': (9, 9, 9),
                 'Z': (9, 9, 9, 9)
                 }
    previous = ''
    for ch in text:
        if char_nums[ch.upper()][-1] == char_nums[previous.upper()][0]:
            nums.append(-1)
        for n in char_nums[ch.upper()]:
            nums.append(n)
        previous = ch
    return nums


def normalization(angle):
    while angle > 359:
        angle -= 360
    while angle < 0:
        angle += 360
    return angle


def nums_to_angle(nums):
    angle = 0
    base_angle = 30
    angle = sum(nums) * base_angle
    return normalization(angle)


def round_angle(angle):
    angle = normalization(angle)
    if 0 <= angle <= 15:
        return 0
    elif 15 < angle <= 45:
        return 30
    elif 45 < angle <= 75:
        return 60
    elif 75 < angle <= 105:
        return 90
    elif 105 < angle <= 135:
        return 120
    elif 135 < angle <= 165:
        return 150
    elif 165 < angle <= 195:
        return 180
    elif 195 < angle <= 225:
        return 210
    elif 225 < angle <= 255:
        return 240
    elif 255 < angle <= 285:
        return 270
    elif 285 < angle <= 315:
        return 300
    elif 315 < angle <= 345:
        return 330
    else:
        return 0


def angles_to_nums(angles):
    nums = []
    for a in angles:
        a = round_angle(a)
        if not a == 0:
            a /= 30
            nums.append(a)
    return nums


def is_phone_tastic(word):
    lenght=len(word)
    nums=text_to_nums(word)
    return (nums_to_angle(nums)%lenght)==0
