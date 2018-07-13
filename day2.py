
"""
programing
"""
def main():
    """
    start
    """
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    sos = max(num1, num2, num3)
    sos1 = min(num1, num2, num3)
    sos2 = sos-sos1
    print(sos2)

main()
