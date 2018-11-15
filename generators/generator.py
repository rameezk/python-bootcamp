def cube(N):
    for n in range(N):
        yield n**3


cubes = cube(10)

for c in cubes:
    print(c)


s = "hello"

it = iter(s)

print(next(it))
print(next(it))
print(next(it))
