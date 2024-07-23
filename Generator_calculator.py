def num_abb (user_in: str):
    expo = ""
    for i in user_in:
        if i.isalpha():
            expo = "".join([expo, i])
    if expo.lower() == "":
        multi = 1
    if expo.lower() == "k":
        multi = 10**3
    if expo.lower() == "m":
        multi = 10**6
    if expo.lower() == "b":
        multi = 10**9
    if expo.lower() == "t":
        multi = 10**12
    if expo.lower() == "q":
        multi = 10**15
    if expo.lower() == "qi":
        multi = 10**18
    if expo.lower() == "s":
        multi = 10**21
    if expo.lower() == "sx":
        multi = 10**24
    if expo.lower() == "o":
        multi = 10**27
    if expo.lower() == "n":
        multi = 10**30
    if expo.lower() == "d":
        multi = 10**33

    num = ""
    for i in user_in:
        if not i.isalpha():
            num = "".join([num, i])

    float_out = float(num) * multi
    return float_out

input
    
tick = num_abb(input("Generator base ticks: "))
gen = num_abb(input("Generator power per tick: "))
cost = num_abb(input("Generator cost: "))

lvl = 1 
while lvl != 10:    
    print(f"{int(((tick * lvl * gen) - cost) // (tick * lvl))} average cost per tick at level {lvl}") 
    lvl += 1
