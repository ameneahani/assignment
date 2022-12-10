# Stor application
import qrcode
PRODUCTS =[]

def read_from_database():
    f =open("database.txt",'r')
    for line in f:
        result=line.split(",")
        my_dict = {'code':result[0],'name':result[1],'price':result[2],'count':result[3]}
        PRODUCTS.append(my_dict)
    f.close()

def write_to_database():
    f=open("database.txt",'w')
    for product in PRODUCTS:
        f.write(product['code']+',')
        f.write(product['name']+',')
        f.write(product['price']+',')
        f.write(product['count'])
    f.close()

def show_menu():
    print("1- Add")
    print("2- edit")
    print("3- remove")
    print("4- Search")
    print("5- Show list")
    print("6-Buy")
    print("7-Make Qr Code")
    print("8-Exit")


def add():
    code=input("enter code:")
    name=input("enter name:")
    price=input("enter price:")
    count=input("enter count:")
    new_product={'code':code,'name':name,'price':price,'count':count}
    PRODUCTS.append(new_product)

def edit():
    code_input = input("enter code of the product: ")
    for product in PRODUCTS:
        if code_input == product['code']:
            print('code\tname\tprice\tcount')
            print(product['code'],'\t',product['name'],'\t',product['price'],product['count'])
            user_choi = int(input("which field do you  want to modify : 1- Name , 2- price , 3-count : "))
            if user_choi == 1:
                new_name=input("enter new name :")
                product['name']=new_name
            elif user_choi == 2:
                new_price=input("enter new price :")
                product['price']=new_price
            elif user_choi == 3:
                new_count=input("enter new count :")
                product['count']=new_count
            else:
                print("Invalid input")
            print("Information update successfully ")    
            break
    else:
        print("The code not found")

def remove():
    input_code = input("enter the code:")
    i=0
    for product in PRODUCTS:
        if product['code'] == input_code:
            PRODUCTS.pop(i)
            print("Removed successfully")
            break
        i += 1
    else:
        print("The code not found")


def search():
    user_input=input("enter the name or code of product: ")
    for product in PRODUCTS:
        if user_input in product['name'] or user_input in product['code']:
            print('code\tname\tprice')
            print(product['code'],'\t',product['name'],'\t',product['price'])
            break
    else:
        print("The product isnt exist")

def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t",product["name"], "\t\t",product["price"])

def buy():
    CART=[]
    input_code=0
    while input_code != "end":
        input_code=input("enter code of the product or type end:")
        for product in PRODUCTS:
            if input_code == product['code']:
                n=int(input("How many of this product do you want : "))
                product['count']=int(product['count'])
                if n > product['count']:
                    print("the number that you want isnt exist ")
                    break
                elif n <= product['count']:
                    product['count']=product['count']-n
                    cart_dict={'name':product['name'],'price':product['price'],'count':n}
                    CART.append(cart_dict)
                    print("Successfully added to cart")
                    break
                else:
                    print("Invalid input try again")
                    break
        else:
            if input_code != "end":
                print("The code not found")
    print("product\t\tprice\t\tcount\t\tTotal")
    for product in CART:
        print(product['name'],'\t\t',product['price'],'\t\t',product['count'],'\t\t',product['count']*int(product['price']))


def make_qrcode():
    input_code = input("enter the code: ")
    for product in PRODUCTS:
        if input_code == product['code']:
            img=qrcode.make('code: '+product['code']+'\nname: '+product['name']+'\nprice: '+product['price'])
            img.save(product['code']+'.png')
            print("Successfully done")
            break
    else:
        print("The code not found")



print("Welcome to my store")
print("Loading...") 
print("Data loaded")
read_from_database()

while True:
    show_menu()
    choise = int(input("enter your choice: "))
    if choise == 1 :
        add()
    elif choise == 2:
        edit()
    elif choise == 3:
        remove()
    elif choise == 4:
        search()
    elif choise == 5:
        show_list()
    elif choise == 6:
        buy()
    elif choise == 7:
        make_qrcode()
    elif choise == 8:
        write_to_database()
        exit(0)
    else:
        print("Invalid input try again")











