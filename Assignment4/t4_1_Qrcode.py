import qrcode
print("wellcome to Qr code image generator")
# data=[]

# data.append(input("enter your name please:"))
# data.append(input("enter your mobile number please:"))
name=input("enter your name please:")
mobile_number=input("enter your mobile number please:")
img=qrcode.make(name + ":" + mobile_number)
img.save("name_mobile_qrcode.png")