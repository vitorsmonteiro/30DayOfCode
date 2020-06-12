Day 8: Dictionaries and Maps

# Enter your code here. Read input from STDIN. Print output to STDOUT
def getinputs(n):
    phone_book = {}
    for i in range(n):
        text = input()
        name = text.split(sep = " ")[0]
        number = text.split(sep = " ")[1]
        phone_book[name] = number
    return phone_book

def check_phone(name, phone_book):
    if name in phone_book.keys():
        print("{}={}".format(name,phone_book[name]))
    else:
        print("Not found")
    return

n = int(input())

phone_book = getinputs(n)

while True:
    try:
        name = input()
        check_phone(name, phone_book)
    except:
        break
