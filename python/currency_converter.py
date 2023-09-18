def rupee(doller):
    print(doller/0.012,"Rupees")
def doller(rupee):
    print(rupee*0.012 ,"Dollers")

while True:
    print("A-->Rupee to Doller")
    print("B-->Doller to Rupee")
    ch = input("Enter the choise:")
    if(ch.lower()=="a"):
        rupee = float(input("Enter Rupee:"))
        doller(rupee)
    elif(ch.lower()=="b"):
        doller = float(input("Enter Doller:"))
        rupee(doller)
    else:
        print("Enter a valid choise")