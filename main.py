def afisare_menu():
    print("1.Citire date")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea:Toate numerele sunt pătrate perfecte.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea:Toate numerele au același număr de divizori.")
    print("4.Ieșire.")
def citire_date():
    lst = input("lista de nr este(cu virgula intre elemente): ")
    lst = lst.split(",")
    lst = [int(el) for el in lst]
    return lst
def patrat_perfect(n):
    for i in range(1,n+1):
        if i*i==n:
            return True
    return False
def get_longest_all_perfect_squares(lst):
    lmax=0
    l=0
    j=-1
    for i,el in enumerate(lst):
        if patrat_perfect(el)== True:
            l=l+1
        else :
            l=0
        if lmax<l:
            lmax=l
            j=i
    rez=[]
    for i in range(j-lmax+1,j+1):
        rez.append(lst[i])
    return rez

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1,2,3,4,5,16,36,64,121,5]) == [16,36,64,121]
    assert get_longest_all_perfect_squares([7,11,19,-3,0]) == []
    assert get_longest_all_perfect_squares([4,9,16,25,17,1,4,4,9,36,400]) == [1,4,4,9,36,400]
test_get_longest_all_perfect_squares()

def divizori(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt=cnt+1
    return cnt
def get_longest_same_div_count(lst):
    lmax=0
    l=0
    j=-1
    nrdiv=-1
    for i,el in enumerate(lst):
        if divizori(el)==nrdiv:
            l=l+1
        else:
            l=1
            nrdiv=divizori(el)
        if lmax<l :
            lmax=l
            j=i
    rez = []
    for i in range(j - lmax + 1, j + 1):
        rez.append(lst[i])
    return rez
def test_get_longest_same_div_count() :
    assert get_longest_same_div_count([4,7,11,17,19,22,32]) == [7,11,17,19]
    assert get_longest_same_div_count([5,4,9,25,121,169,74,0]) ==[4,9,25,121,169]
    assert get_longest_same_div_count([6,77,39,35]) == [6,77,39,35]
test_get_longest_same_div_count()

def start():
    lst=[]
    while True:
        afisare_menu()
        optiune=int(input("Selectati optiunea: "))

        if optiune==1:
            lst=citire_date()
        elif optiune==2:
            rez=get_longest_all_perfect_squares(lst)
            print("Subsecventa este: ",rez)
        elif optiune==3:
            rez=get_longest_same_div_count(lst)
            print("Subsecventa este: ",rez)
        else:
            break
start()

