"""
programing
"""
def main():
    """
    start
    """
    num1 = int(input())
    print("Price\t%.2f THB"  %num1)
    print("Service\t%.2f THB" %(num1*0.10))
    print("VAT\t%.2f THB" %((num1*110/100)*(0.08)))
    print("Total\t%.2f THB" %((num1*110/100)*(0.08)+(num1*0.10)+(num1)))
main()
