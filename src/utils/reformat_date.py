def replace_fillz(input : str ="") :
    val = input.split(".")
    
    if len(val) == 3 :
       return  val[0]+'-'+(val[1].zfill(2))+'-'+(val[2].zfill(2)) 

    return  val[0]+'-'+(val[1].zfill(2))

def concatenate_date(year = "", month = "", date ="") :
    if(date == ""):
        return str(year) + '.' + str(month).zfill(2)

    return str(year) + '.' + str(month).zfill(2)+ '.' + str(date).zfill(2)