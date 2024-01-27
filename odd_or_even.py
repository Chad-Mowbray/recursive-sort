# params: integer
# return: boolean


# Solution must be recursive.  Can't use division


cache = {}

def add(a,b):
    if (a,b) in cache:
        print(f"got value from cache: {a}, {b}")
        return cache[(a,b)]
    else:
        result = a + b
        cache[(a,b)] = result
        return result
    
    
if __name__ == "__main__":
    add1 = add(1,2)
    add2 = add(2,3)
    add3 = add(1,2)
    print(add1, add2, add3)