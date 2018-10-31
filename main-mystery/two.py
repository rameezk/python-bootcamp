import one

print("top level in two")

one.my_func()

if __name__ == "__main__":
    print("running two directly")
else:
    print("two is being imported")
