import bs4 as bs
import requests
import os
from tqdm import tqdm
import json   
import pyperclip
import time
import dictdiffer  
import traceback                                        

debug_write_to_file = False

endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

endpoint = requests.head(endpoint, allow_redirects=True, timeout=10)

assert endpoint.status_code == 200

endpoint = endpoint.url

print(endpoint)

while True:

    url = endpoint
    
    url = "https://w5.ab.ust.hk/wcq/cgi-bin/2210/"

    page = requests.get(url, timeout=10)

    assert page.status_code == 200

    soup = bs.BeautifulSoup(page.text,'lxml')

    depts = soup.select('.depts')[0]
    
    depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
    depts_plus_dict = dict(depts_plus)
    depts = depts.get_text("\n").split("\n")
    
    print(depts_plus)
    input()
    os.system("cls")

    allcourses_dict = {}

    for dept in (depts):

        url = '{}subject/{}'.format("https://w5.ab.ust.hk/wcq/cgi-bin/2210/", dept)
        
        #url = "http://localhost:8000/{}".format(dept)

        page = requests.get(url, timeout=10)
        
        assert page.status_code == 200
        
        if debug_write_to_file:
            with open(dept, "w", encoding="utf-8") as rf:
                rf.write(page.text)

        soup = bs.BeautifulSoup(page.text,'lxml')

        courses = soup.select('#classes > .course')
        
        
        buffered_coursetable_row = []
        
        for course in courses:
            course_flags = []
            coursetitle = course.select("h2")[0].decode_contents()
            
            courseinfo_bar = course.select(".courseinfo > div")
            
            for elem in courseinfo_bar[:-1]:
                print(elem.get_text(separator=": "))
                course_flags.append(elem.get_text(separator=": "))
                
            course_flags.sort()
            
            courseinfo = course.select(".courseattr.popup > .popupdetail > table")
            try:
                assert len(courseinfo) == 1
                courseinfo = courseinfo[0]
                courseinfo_dict = {}
                for row in courseinfo.select("tr"):
                    if len(row.find_parents("table")) == 1:
                        thead = row.select("th")[0].get_text(separator="_")
                        tcontent = row.select("td")[0].get_text(separator=" ")
                        courseinfo_dict[thead] = tcontent
                    else: 
                        pass
            except:
                courseinfo_dict = {"FAILURE":"course_popup_table_count_mismatch", "TABLE_COUNT":len(courseinfo)}
            coursetable = course.select("table.sections")
            course_table_length_mismatch = False
            try:
                assert len(coursetable) == 1
            except:
                coursetable_len = len(coursetable)
                course_table_length_mismatch = True
            coursetable = coursetable[0]
            coursetable_list_dicts = []
            keys = coursetable.select('tr')[0].select("th")
            keys = [k.text.replace(" & ", "_N_") for k in keys]
            for row in coursetable.select('tr')[1:]:
                fields = row.select("td")
                
                if buffered_coursetable_row and len(fields) == 3: # is an extension
                    buffered_coursetable_row_2 = [None for i in range(len(buffered_coursetable_row))]
                    buffered_coursetable_row_2 = ["" for i in range(len(buffered_coursetable_row))]
                    buffered_coursetable_row_2[1] = "; {}".format(fields[0].get_text(separator="_"))
                    buffered_coursetable_row_2[2] = "; {}".format(fields[1].get_text(separator="_"))
                    buffered_coursetable_row_2[3] = "; {}".format(fields[2].get_text(separator="_"))
                    #print(buffered_coursetable_row, buffered_coursetable_row_2)
                    buffered_coursetable_row = [i if not isinstance(i, str) else str(i)+str(k) for i,k in zip(buffered_coursetable_row, buffered_coursetable_row_2)]
                    continue # we are done
                else:
                    if buffered_coursetable_row:
                        coursetable_list_dicts.append(dict(zip(keys,buffered_coursetable_row)))
                        buffered_coursetable_row = []
                    if len(buffered_coursetable_row) < len(fields):
                        buffered_coursetable_row = [None for i in range(len(fields))]
                    for i, field in enumerate(fields):
                        if field.select("span") and i == 4:
                            buffered_coursetable_row[i] = field.select("span")[0].text
                        elif i in (0,1,2,3,4,5,6,7):
                            buffered_coursetable_row[i] = field.get_text(separator="_")
                        elif i in (8,):
                            mkdict = {}
                            if field.select(".popup.consent"):
                                mkdict["consent"] = True
                            else:
                                mkdict["consent"] = False
                            if field.select(".popup.classnotes"):
                                mkdict["info"] = ''.join(field.select(".popup.classnotes")[0].get_text(separator="; ").splitlines()) # no need newlines here. 
                            buffered_coursetable_row[i] = mkdict
                #coursetable_list_dicts.append(dict(zip(keys,field2)))
            if buffered_coursetable_row:
                coursetable_list_dicts.append(dict(zip(keys,buffered_coursetable_row)))
                buffered_coursetable_row = []
            coursecode = coursetitle.split("-")[0].strip().replace(" ","")
            if course_table_length_mismatch == True:
                allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECTIONS":coursetable_list_dicts, "FAILURE":"course_table_length_mismatch", "TABLE_COUNT":coursetable_len}
            else:
                allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECTIONS":coursetable_list_dicts}


    os.system("cls")
    print(allcourses_dict["MARK5120"]['COURSE_INFO']['INTENDED_LEARNING_OUTCOMES'])
    
    try:
        with open("latest_state.json".format(time.time()),"r") as f:
            allcourses_dict_old = json.load(f)

        #pyperclip.copy(output)
        
        notif = {}
        for diff in list(dictdiffer.diff(allcourses_dict_old, allcourses_dict)):         
            expected_channel_names = ['CENG', 'CIVL', 'COMP', 'DBAP', 'ECON', 'EESM', 'ELEC', 'ENGG', 'ENTR', 'ENVR', 'EVSM', 'GFIN', 'ISDN', 'ISOM', 'LIFS', 'MAFS', 'MARK', 'MASS', 'MGCS', 'PHYS', 'SBMT', 'SOSC', 'TEMG']
            for expected_channel_name in expected_channel_names:
                if expected_channel_name in diff[1][0] or expected_channel_name in diff[1]:
                    notif[expected_channel_name] = notif.get(expected_channel_name, []) + [diff]
                    break
            else: # no break
                notif["MISC"] = notif.get("MISC", []).append(diff)

        print(notif)

    except Exception as e:
        print(traceback.format_exc())
        print(e)
        
    with open("latest_state.json".format(time.time()),"w") as f:
        json.dump(allcourses_dict, f)
    
    #time.sleep(300)

