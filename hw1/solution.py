def calculate_final_vector(start_point, list_of_colors):
    end_point = [start_point[0] , start_point[1]]

    for color in list_of_colors:
        # up [1]+1 down [1]-1 left [0]-1 right [0]+1
        match color.upper():
            case 'C0FFC0':  # right -1
                end_point[0] -= 1
            case 'FFFFC0':  # up -1
                end_point[1] -= 1
            case 'FFC0C0':
                end_point[0] += 1  # left -1
            case 'C0C0FF':  # down -1
                end_point[1] += 1
            case '00C000':  # right +1
                end_point[0] += 1
            case 'C0C000':  # up +1
                end_point[1] += 1
            case 'C00000':  # left +1
                end_point[0] -= 1
            case '0000C0':  # down +1
                end_point[1] -= 1
            case 'FFFFFF':  # nop
                continue
            case '000000':  # end
                a = (end_point[0], end_point[1])
                return a
            case _:  # default
                print('Error: {0} is not valid color'.format(color))

    a = (end_point[0], end_point[1])
    return a
