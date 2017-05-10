def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
def speak_excitedly(message, num_exclamations=1, enthusiasm=False):
    message += '!' * num_exclamations
    if not enthusiasm:
        return message
    return message.upper()
def test_speak_excitedly():
    print(speak_excitedly("I love Python"))
    print(speak_excitedly("Keyword arguments are great", num_exclamations=4))
    print(speak_excitedly("I guess Java is okay...", num_exclamations=0))
    print(speak_excitedly("Let's go Stanford", num_exclamations=2, enthusiasm=True))

def average(*nums):
    if not nums: return None
    return sum(nums) / len(nums)
    
def say_hello():
    print("Hello!")
def echo(arg=None):
    print("arg:", arg)
    return arg
def drive(has_car):
    if not has_car:
        return
    return 100  # miles
