def main():
    l = []
    integer = int(input("Enter a number : "))
    for i in range(integer):
        n = input("Enter a number : ")
        if n == 0:
            l.append('False')
        else:
            try:
                if float(n) and n != 0:
                    l.append('True')
                else:
                    l.append('False')
            except:
                l.append('False')
    print('\n'.join(l))


