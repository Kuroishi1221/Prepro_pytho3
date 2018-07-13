"""
pre
"""
def main():
    """main"""
    pizza = int(input())
    size = int(input())

    tray = pizza/size
    result = int(tray) + int(tray % 1 > 0)
    print(result)
main()
