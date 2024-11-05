def show(n):
    if n==0:return
    print(n,end=' ')
    show(n-1)
show(5)

print()
print("************************** Factorial **************************")

def fact(n):
    if (n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(4))

print("******************* First n natural numbers *******************")

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)

print("**************** print all elements in a list ****************")

l = [111,21,73,47,50]
def print_elem(l,i):
    if i >= len(l):
        return 1
    print(l[i],end=' ')
    print_elem(l,i+1)

print_elem(l,0)
