status=input("enter your status")
if status=="delivered":
    print("your order has been successfully delivered")
elif status=="sent":
    print("your order is on the way")
elif status=="registered":
    print("your order is being processed")
else:
    print("status unknown")
