class Adding:
    def __init__(self, name):
        print("name ", name)
        

    def __sub__(self, b):
        return b
    
a = Adding("manoj")

print(a.__sub__(2 - 1))

