'''quota_testing = {"Quota": 10320, "Enrol": 62, "Avail": 13}

def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))
   
   
# printTable([quota_testing])'''
def beautify(quota, skipheader=False):
    outstr = ""
    if not skipheader:
        outstr += "  |".join(str(x).rjust(7," ") if len(str(x)) <= 7 else "999999 " for x in quota.keys())
        outstr += "\n"
    outstr += "  |".join(str(x).rjust(7," ") if len(str(x)) <= 7 else "999999 " for x in quota.values())
    return outstr
    
    
def uglify(quota_string):
    outstr1, outstr2 = quota_string.split("\n", 1)
    outstr1 = " ".join(outstr1.split())
    outstr2 = " ".join(outstr2.split())
    return {k.strip():int(v.strip()) for k,v in zip(outstr1.split("|"), outstr2.split("|"))}
    
def is_string_QEA(string):
    try:
        return is_dict_QEA(uglify(string))
    except:
        return False
        
def is_dict_QEA(dict_in):
    try:
        assert len(dict_in.keys()) == 3
        assert set(dict_in.keys()) == set(("Quota","Enrol","Avail"))
        (int(x) for x in dict_in.values())
        return True
    except:
        return False
    
    
def is_QEA(generic_in):
    return is_string_QEA(generic_in) or is_dict_QEA(generic_in)
    
    
# print(beautify(quota_testing))

def signed_diff(int1, int2):
    diff = int1 - int2
    if not diff:
        return ""
    sign = "+" if diff >0 else ""
    return "{}{}".format(sign, diff)

def diff_between_QEA(QEA1, QEA2): #old, new
    return "\n".join((beautify(QEA1),"  |".join(signed_diff(x,y).rjust(7," ") if len(signed_diff(x,y)) <= 7 else "###### " for x, y in zip(QEA2.values(), QEA1.values())),"  |".join("=".rjust(7," ") for _ in range(3)),beautify(QEA2, skipheader=True)))

if __name__ == "__main__":  
    print(diff_between_QEA({"Quota": 103200, "Enrol": 62, "Avail": 13}, {"Quota": 0, "Enrol": 103200, "Avail": 0}))
    
    