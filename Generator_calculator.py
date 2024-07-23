def num_abb (user_in: str):
    expo = ""
    for i in user_in:
        if i.isalpha():
            expo = "".join([expo, i])
    
    multi = 1
    table = {"": 0, "k": 3, "m": 6, "b": 9, "t": 12, "q": 15, "qi": 18, "s": 21, "sx": 24, "0": 27, "n": 30, "d": 33}
    for abbr, expon in table.items():
        if expo.lower() == abbr:
            multi = 10 ** expon

    num = ""
    for i in user_in:
        if not i.isalpha():
            num = "".join([num, i])

    float_out = float(num) * multi
    return float_out

tick = num_abb(input("Generator base ticks: "))
gen = num_abb(input("Generator power per tick: "))
cost = num_abb(input("Generator cost: "))

lvl = 1 
while lvl != 10:    
    print(f"{int(((tick * lvl * gen) - cost) // (tick * lvl))} average cost per tick at level {lvl}") 
    lvl += 1
