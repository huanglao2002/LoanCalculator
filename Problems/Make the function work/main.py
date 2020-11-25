def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
#   elif x % 5 <= 2:
#       y = x - (x % 5)
#       return y
    else:
        return x + (5 - (x % 5))
