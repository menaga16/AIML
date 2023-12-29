#towers of hanoi
def index(arr, n):
    i=len(arr)-1
    while(i>=0):
        if(arr[i]==n):
            return i
        i-=1
    return 0

def bottom(arr):
    i=len(arr)-1
    while(i>=0):
        if(arr[i]=="-"):
            return i
        i-=1
    return 0

def remove(n, src, aux, dest, s, d):
    if(s =='A'):
        src[index(src, n)] = "-"
    if(s == 'B'):
        aux[index(aux, n)] = "-"
    if(s == 'C'):
        dest[index(dest, n)] = "-"

    if(d=='A'):
        src[bottom(src)]= n
    if(d=='B'):
        aux[bottom(aux)]= n
    if(d=='C'):
        dest[bottom(dest)]= n

def display(n, src, aux, dest):
    print("A B C")
    for i in range(0,n):
        print(f"{src[i]} {aux[i]} {dest[i]}")
    print()

def move(n, disc, src, aux, dest, s, a, d):
    if(n==1):
        print(f"move disk {n} from {s} to {d}")

        remove(n, src, aux, dest, s, d)
        display(disc, src, aux, dest)
        return
    else:
        move(n-1,disc, src, aux, dest, s, d, a)
        print(f"move disk {n} from {s} to {d}")

        remove(n, src, aux, dest, s, d)
        display(disc, src, aux, dest)

        move(n-1,disc, src, aux, dest, a, s, d)

n=int(input("enter number of disk : "))
src=[]
aux=[]
dest=[]
for i in range(0,n):
    src.append(i+1)
    aux.append("-")
    dest.append("-")

display(n, src, aux, dest)
move(n, n, src, aux, dest, 'A', 'B', 'C')
