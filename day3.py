"""
programing
"""
def main():
    """resolution"""
    money = int(input())
    price = int(input())

    change = money - price  #ttl change

    print(change//100) #count 100-nt
    change = change % 100 #Remove 100-nt

    print(change//50) #count 50-nt
    change = change % 50 #Remove 50-nt

    print(change//20)# count 20-nt
    change = change % 20 #Remove 20-nt

    print(change//10) #count 10-nt
    change = change % 10 #Remove 10-nt

    print(change//5) #count 5-nt
    change = change % 5 #Remove 5-nt

    print(change//2) #count 2-nt
    change = change % 2 #Remove 2-nt

    print(change//1) #count 1-nt
    change = change % 1 #Remove 1-nt

main()
