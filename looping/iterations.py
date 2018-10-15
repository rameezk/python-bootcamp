for letter in "hello":
    print (letter)


# Tuple unpacking
t = [(1,2), (3,4), (5,6)]
for a, b in t:
    print(a)
    print(b)

# Looping through dictionaries
print("\nLooping through dictionary")
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(f'key={key} value={value}')
