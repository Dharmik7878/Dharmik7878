class dhamo(Exception):
    pass

def risky_function():
    raise dhamo("Something went wrong in risky_function")

try:
    risky_function()
except dhamo as e:
    print(e)
