import math 

colors = [
'#a2a8a7',
'#5b5b5b',
'#444444',
'#999999',
'#bcbcbc'
]

def check_if_color_gray_variation(input_color):

    '''
    Input can either be color name or hex code
    '''

    if type(input_color)==str:
        if 'gray' in input_color.lower():
            return True

    input_color = tuple(int(input_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    for i in range (len(colors)):
        use_color = colors[i]

        my_color = tuple(int(use_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        get_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(my_color, input_color)]))
        #print(get_distance)
        if get_distance <30.0:
            return True
        
    return False








