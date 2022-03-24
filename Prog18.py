#Write a script to enter five string in a list and check print string whose lenth has even number of character
def createlist():
    l=[]
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
    return(l)
s =createlist()
for i in s:
    print(i)

    

    


        
