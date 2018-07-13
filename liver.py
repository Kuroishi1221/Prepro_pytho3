"""
1st preprogram
Ratchanon
6456454
"""
def main():
    """ohoh"""
    start = int(input())
    info_five(start)
    info_five(start+5)
    info_five(start+10)
    info_five(start+15)
    info_five(start+20)
    info_five(start+25)
    info_five(start+30)
    info_five(start+35)
    info_five(start+40)
    info_five(start+45)

def info_five(start):
    """sdad"""
    name_a = input()
    name_b = input()
    name_c = input()
    name_d = input()
    name_e = input()

    print("ID#%d\t%s" %(start, name_a))
    print("ID#%d\t%s" %(start+1, name_b))
    print("ID#%d\t%s" %(start+2, name_c))
    print("ID#%d\t%s" %(start+3, name_d))
    print("ID#%d\t%s" %(start+4, name_e))

main()
