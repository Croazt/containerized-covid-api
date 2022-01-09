import re

def check_params_pattern(is_type : str, params : str):
    value = params.split('.')
    pattern_year = re.compile('^[0-9][0-9][0-9][0-9]')
    pattern_md_1 = re.compile('^[0-9][0-9]')
    pattern_md_2 = re.compile('^[0-9]')
    
    checker = False
    if is_type == 'year' :     
        if pattern_year.match(value[0]) :
            checker =  True
    if is_type == 'month' :     
        if pattern_year.match(value[0]) and (pattern_md_1.match(value[1]) or pattern_md_2.match(value[1])) :
            checker =  True
    if is_type == 'date' :     
        if pattern_year.match(value[0]) and (pattern_md_1.match(value[1]) or pattern_md_2.match(value[1])) and (pattern_md_1.match(value[2]) or pattern_md_2.match(value[2])):
            checker =  True
    
    return checker