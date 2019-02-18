def between(value, a, b):
    pos_a = value.find(a)
    if pos_a == -1: 
        return ""
    pos_b = value.rfind(b)
    if pos_b == -1: 
        return ""
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: 
        return ""
    return value[adjusted_pos_a:pos_b]

def before(value, a):
    pos_a = value.find(a)
    if pos_a == -1: 
        return ""
    return value[0:pos_a]

def after(value, a):
    pos_a = value.rfind(a)
    if pos_a == -1: 
        return ""
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): 
        return ""
    return value[adjusted_pos_a:]

def file_to_list(in_file):
    file_in = open(in_file,"r")
    in_list = file_in.read().splitlines()
    file_in.close()
    return in_list