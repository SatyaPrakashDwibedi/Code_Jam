testcases=input()
def group(s):
    temp=s[0]
    counter=0
    for t in s:
        if t==temp:
            pass
        else:
            temp=t
            counter=counter+1
    #print(counter)
    return counter

for j in range(testcases):
    i=raw_input()
    n=group(i)
    if i[0]=='+' and i[-1]=='+':
        print("Case #"+str(j+1)+': '+str(n))
    elif i[0]=='+' and i[-1]=='-':
        print("Case #"+str(j+1)+': '+str(n+1))
    elif i[0]=='-' and i[-1]=='+':
        print("Case #"+str(j+1)+': '+str(n))
    else:
        print("Case #"+str(j+1)+': '+str(n+1))
        
