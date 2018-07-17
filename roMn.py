"""romann"""
def main():
    """fm"""
    text= input()
    roman = {'I':'1', 'V':'5', 'X':'10', 'L':'50','C':'100', 'D':'500', 'M':'1000'}
    for i in text:
        if i in roman:
            print(roman.keys())
main()

