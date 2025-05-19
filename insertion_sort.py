def insertion_sort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while i>=0 and key>a[i]:
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
    return a

if __name__=="__main__":
    a=[2,6,1,9,4,8,5,0]
    b=insertion_sort(a)
    print(b)