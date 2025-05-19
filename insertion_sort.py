def insertion_sort(a):  # python program for insertion sort in desecnding order
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
    c=[9,1,10,111]
    d=insertion_sort(c)
    print(d)