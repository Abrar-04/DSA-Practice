# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

def duplicate(str):
    count={}

    for s in str:
        if s in count:
            count[s]+=1
        else:
            count[s]=1

    return count

str1='geeksforgeeks'
print(duplicate(str1))



