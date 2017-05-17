def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))


def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

    
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

def speak_excitedly(a,b=1,c=False):
    a += '!' * b
    if (c==True):
        print(a.upper())
    else:
        print(a)
