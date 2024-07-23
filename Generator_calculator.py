def num_abb (user_in: str):
    expo = ""
    for i in user_in:
        if i.isalpha():
            expo = "".join([expo, i])
    if expo.lower() == "":
        multi = 1
    if expo.lower() == "k":
        multi = 1*10**3
    if expo.lower() == "m":
        multi = 1*10**6
    if expo.lower() == "b":
        multi = 1*10**9
    if expo.lower() == "t":
        multi = 1*10**12
    if expo.lower() == "q":
        multi = 1*10**15
    if expo.lower() == "qi":
        multi = 1*10**18
    if expo.lower() == "s":
        multi = 1*10**21
    if expo.lower() == "sx":
        multi = 1*10**24
    if expo.lower() == "o":
        multi = 1*10**27
    if expo.lower() == "n":
        multi = 1*10**30
    if expo.lower() == "d":
        multi = 1*10**33

    num = ""
    for i in user_in:
        if not i.isalpha():
            num = "".join([num, i])

    float_out = float(num) * multi
    return float_out

input
    
tick = num_abb(input("Generator ticks: "))
gen = num_abb(input("Generator power per tick: "))
cost = num_abb(input("Generator cost: "))

lvl = 1 
while lvl != 10:    
    print(f"{int(((tick * lvl * gen) - cost) // (tick * lvl))} energy per tick at level {lvl}") 
    lvl += 1
