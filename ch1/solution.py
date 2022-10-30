def suffix(num):
    match num[-1]:
        case "1":
            return num + "st"
        case "2":
            return num + "nd"
        case "3":
            return num + "rd"
        case _:
            return num + "th"


def suffix_ordinals(nums):
    numbers = nums.split(".")
    output = ""
    for n in numbers:
        if len(n) > 1:
            if n[-2] == "1":
                output += n + "th"
            else:
                output += suffix(n)
        else:
            output += suffix(n)
        if n is not numbers[-1]:
            output += " of the "
    print(output)
    return output
