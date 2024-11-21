name = input()
marks = int(input())
if(marks>=90):
    print(f"{name} secured A grade")
elif(80<=marks<=89):    
    print(f"{name} secured B grade")
elif(70<=marks<=79):
    print(f"{name} secured C grade")
elif(60<=marks<=69):
    print(f"{name} secured D grade")
else:
    print("fail")
    