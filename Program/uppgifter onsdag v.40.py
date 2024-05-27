def uppgift_1():
    x = "He was going to live forever, or die in the attempt."
    y = x.count("e")
    print(y)

def uppgift_2():
    mittnamn = "Erik"
    print(mittnamn[::-1])

def uppgift_3():
    mittnamn = "Erik"
    mittnamn = mittnamn.lower()
    v = "aouåeiyäö"
    for hmm in v:
        if hmm in v:
            mittnamn = mittnamn.replace(hmm, "")
    print(mittnamn)

def uppgift_4():
    mittnamn = input("")
    mittnamn = mittnamn.lower()
    k = "cdfghjklmnpqrstvwxz"
    for hmm in mittnamn:
        if hmm in k:
            mittnamn = mittnamn.replace(hmm, hmm + "o" + hmm)
            k = k.replace(hmm, "")
    print(mittnamn)

uppgift_4()
