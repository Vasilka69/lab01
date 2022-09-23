
def NOD(a, b):
    while a != 0 and b != 0:
        if a > b: 
            a = a-b
        else: 
            b = b-a
    return max(a, b)

def main():
    print(NOD(30, 24))

main()