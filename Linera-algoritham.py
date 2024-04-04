
env = ["dev","stage","production"]

key = "stg"
is_found = False

for i in env:
    if i == key:
       is_found = True

if is_found == True:
    print("found")
else:
    print("Not found")
