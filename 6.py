MONTHS = ["Janeiro", "Fevereiro" ,"Março", "Abril", "Maio", "Junho","Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def calc_temp_media(temps):
    return sum(temps)/ len(MONTHS)

def over_media(temp_media, temps):
    over = []
    for i in range(len(MONTHS)):
        over_media  = {}
        if temps[i] > temp_media:
            over_media["MONTH"] = MONTHS[i]
            over_media["TEMP"] = temps[i]
            over.append(over_media)

    return over

if __name__ == '__main__': 
    temp = []
    for month in MONTHS:
        temp.append(float(input("Digite a temperatura média do mês {}: ".format(month))))

    temp_media = calc_temp_media(temp)
    over_media = over_media(temp_media, temp)

    result = ""
    for element in over_media:
        result += " - {} - {} ".format(element["MONTH"], element["TEMP"])
        
    print(temp_media)
    print(result)