def input_number_abbreviation(user_input: str):
    input_abbreviation = ""
    for i in user_input:
        if i.isalpha():
            input_abbreviation = "".join([input_abbreviation, i])
    
    multiplier = 1
    abbreviation_table = {"": 0, "k": 3, "m": 6, "b": 9, "t": 12, "q": 15, "qi": 18, "s": 21, "sx": 24, "0": 27, "n": 30, "d": 33}
    for suffix, exponent in abbreviation_table.items():
        if input_abbreviation.lower() == suffix:
            multiplier = 10 ** exponent

    number = ""
    for i in user_input:
        if not i.isalpha():
            number = "".join([number, i])

    float_out = float(number) * multiplier
    return float_out

def output_number_abbreviation(number_out: int):
    output_length = len(str(number_out))
    if output_length >= 4:
        divided_number = str(number_out / (10 ** (((output_length - 1) // 3) * 3)))
    if output_length <= 4:  
        divided_number = str(number_out)
    abbreviation_table = {"": 0, "k": 3, "m": 6, "b": 9, "t": 12, "q": 15, "qi": 18, "s": 21, "sx": 24, "0": 27, "n": 30, "d": 33}
    for suffix, exponent in abbreviation_table.items():
        if (((output_length - 1) // 3) * 3) == exponent:
            if not len(divided_number) >= 6:
                divided_number = divided_number + "000000"
            if int(divided_number[5]) > 0:
                divided_number = divided_number[:4] + str(int(divided_number[4]) + 1)
            
            abbreviated_number = divided_number[:5] + suffix
            return abbreviated_number   
   
tick = input_number_abbreviation(input("Generator base ticks: "))
heat = input_number_abbreviation(input("Generator heat per tick: "))
cost = input_number_abbreviation(input("Generator price: "))

level = 0
while level != 10:    
    average = int(((tick * (2 ** level) * heat) - cost) // (tick * (2 ** level)))
    print(f"{output_number_abbreviation(average)} average (rounded) profit per tick at level {level}") 
    level += 1
