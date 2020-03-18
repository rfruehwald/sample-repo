import requests


print (sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("http://www.flieg-maxi-flieg.de")
print(r.status_code)
# print (greet("World"))
# print (greet("Ralf"))
