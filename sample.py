name = input()
age = int(input())
if(age>=18):
    print("eligible to vote")
else:
    c=18-age
    print(f"{name} have to comeback after {c} years")