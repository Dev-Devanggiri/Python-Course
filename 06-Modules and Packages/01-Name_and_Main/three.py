import two

print("Inside three.py")

if __name__ == "__main__":
    print("three.py is being run directly")
else:
    print("three.py is being imported into another module")




"""
top-level print inside of one.py
one.py is being imported into another module
top-level in two.py
func() ran in one.py
two.py is being run directly
"""