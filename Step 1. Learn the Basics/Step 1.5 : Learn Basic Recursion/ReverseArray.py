# https://practice.geeksforgeeks.org/problems/reverse-an-array/0

def reverse(l,i,j):
    if(i>=j):
        return l
    l[i],l[j] = l[j],l[i]
    return reverse(l,i+1,j-1)
  
def reverse(l,i):
    if(i>=n//2):
        return l
    l[i],l[n-i-1] = l[n-i-1],l[i]
    return reverse(l,i+1)
