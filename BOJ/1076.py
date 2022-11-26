color1 = input()
color2 = input()
color3 = input()

vals = {'black':0, 'brown':1, 'red':2, 'orange':3,
        'yellow':4, 'green':5, 'blue':6, 'violet':7,
        'grey':8, 'white':9}
rst = vals[color1]*10 + vals[color2]
rst *= 10 ** vals[color3]
print(rst)