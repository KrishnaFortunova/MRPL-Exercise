def f(x) :
    return (x*x)-(x)-20

x1=int(input("Masukkan nilai x1: "))
x2=int(input("Masukkan nilai x2: "))

fX1=f(x1)
fX2=f(x2)

i=1

while fX1*fX2 >= 0 :
    x1 -= i
    fX1=f(x1)
    i += 1

xi=x2-((f(x2)/(f(x2)-f(x1)))*(x2-x1))
fXi=f(xi)

print("I\t\tx1\t\tx2\t\txi\t\tf(x1)\t\tf(x2)\t\tf(xi)")
print(i,x1,x2,xi,fX1,fX2,fXi,sep="\t\t")

while fXi < 0 :
    if fXi < 0 :
        x1=xi
        fX1=fXi
    else :
        x2=xi
        fX2=fXi

    xi=x2-((f(x2)/(f(x2)-f(x1)))*(x2-x1))
    fXi=f(xi)

    print(i,x1,x2,xi,fX1,fX2,fXi,sep="\t\t")

    i += 1

print("\nAkar hampiran: " + str((x1,x2)))