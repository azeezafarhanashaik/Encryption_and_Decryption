def menu(m):
    if m==1:#Encryption
        a=input("Enter your message:")
        k=int(input("Enter a key value(1-10):"))
        s=""
        for i in a:
            l=ord(i)+k
            s=s+chr(l)
        print("The encrypted message is: "+s+"\n")
        print("---------------------------------------------------")
    elif m==2:#Decryptin
        a1=input("Enter your Encrypted message:")
        k1=int(input("Enter the key value:"))
        s1=""
        for i in range(len(a1)):
            l1=ord(a1[i])-k1
            s1=s1+chr(l1)
        print("The Decrypted message is: "+s1+"\n")
        print("---------------------------------------------------")
    elif m==3:#Information
        print("Encryption:\n\nEncryption is like turning your message into a secret code so that only you and your friend can read it,\nkeeping it safe from others who might try to see what it says.\n")
        print("Decryption:\n\nDecryption is like turning your secret code into the encrypted message so that only you and your friend can read it, \nkeeping it safe from others who might try to see what it says.\n")
        print("---------------------------------------------------")
    elif m==4:
        print("Thank you!\nYou are exited now.")
    else:
        print("Enter a valid number")


print("Hello there!")
while (1):
    print("*select work from the menu*")
    print("\t\t1.Encrtpting the data\n\t\t2.Decrypting the data\n\t\t3.Information about Encryption and Decryption\n\t\t4.Exit\n")
    m=int(input("Choose 1/2/3/4: "))
    menu(m)
    if m==4:
        break
