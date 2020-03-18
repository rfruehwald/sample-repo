import requests


r = requests.get("http://www.flieg-maxi-flieg.de")
print(r.status_code)
print(r.ok)

# print (greet("World"))
# print (greet("Ralf"))
