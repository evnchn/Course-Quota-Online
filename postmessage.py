# bot.py

import bs4 as bs
import requests
import os
from tqdm import tqdm
import json   
import pyperclip
import time
import dictdiffer  
import traceback

import asyncio

import os

import discord
from dotenv import load_dotenv

from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

def censor_exception(exception_text):
    splitted = exception_text.split("\n")
    splitted2 = splitted[1].split('"')
    splitted2[1] = "cardinal.py"
    splitted[1] = '"'.join(splitted2)
    return "\n".join(splitted)

def filter_phantom_change(diff):
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
        
    if event == "change":
        if isinstance(content[0], str) and isinstance(content[1], str) and content[0].replace("\r","").replace("\n","") == content[1].replace("\r","").replace("\n",""):
            return False
    return True

def preetify_diff(diff):
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
        
    
        
    if event == "add":
        return "Added from {}: \n{}".format(location, content)
    elif event == "remove":
        return "Removed from {}: \n{}".format(location, content)
    elif event == "change":
        return "Changed {} from: \n{}\nto\n{}".format(location, content[0], content[1])
    else:
        return str(diff)
        
def check_it_out(diff):
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
    cc = location.split(".")[0]
    url = "https://w5.ab.ust.hk/wcq/cgi-bin/2220/subject/{}#{}".format(cc[0:4], cc)
    return url
    
def is_important(diff):
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
    unimportant = ("Enrol", "Avail", "Wait", "COURSE_INFO.DESCRIPTION")
    for unimportant_strings in unimportant:
        if unimportant_strings in location:
            return False
    return True

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
    category_name = 'Bot Zone No. {}{}'.format(0, "-misc")
    category = discord.utils.get(guild.categories, name=category_name)

    if not category:
        await guild.create_category(category_name)
        print("Created category"+category_name)
    else:
        print("Fine, category exists"+category_name)
    for important_preboot_channels in ("debug", "bootlog"):
        channel = discord.utils.get(guild.text_channels, name=important_preboot_channels)
        if not channel:
            try:
                await guild.create_text_channel(important_preboot_channels, category=category)
            except:
                await guild.create_text_channel(important_preboot_channels)
                
                
                
    channels_to_remove = [str(i).rjust(4, "0") for i in range(60)]
    channels_to_remove += [(i+"-important") for i in channels_to_remove]
    #channels_to_remove = '''ceng,civl,comp,dbap,econ,eesm,elec,engg,entr,envr,evsm,gfin,isdn,isom,lifs,mafs,mark,mass,mgcs,phys,sbmt,sosc,temg,ceng-important,civl-important,comp-important,dbap-important,econ-important,eesm-important,elec-important,engg-important,entr-important,envr-important,evsm-important,gfin-important,isdn-important,isom-important,lifs-important,mafs-important,mark-important,mass-important,mgcs-important,phys-important,sbmt-important,sosc-important,temg-important,misc,misc-important,debug,bootlog'''.split(",")
    for channel_name in channels_to_remove:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if channel:
            await channel.delete()
    try:
        debug_write_to_file = False

        endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

        endpoint = requests.head(endpoint, allow_redirects=True).url

        print(endpoint)

        url = endpoint

        page = requests.get(url)

        soup = bs.BeautifulSoup(page.text,'lxml')

        depts = soup.select('.depts')[0]
        
        depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
        depts_plus_dict = dict(depts_plus)
        depts = depts.get_text("\n").split("\n")
        
        expected_channel_names = depts
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)

        channel = discord.utils.get(guild.text_channels, name="debug")
        await channel.send("admin pls help (get_subjects):\n```\n{}\n```\n{}".format(exception_text, e))
        expected_channel_names = ['ISDN']
    
    expected_channel_names = [i.lower() for i in expected_channel_names]
    
    expected_channel_names = expected_channel_names + [(i+"-important") for i in expected_channel_names]
    # only lowercase letters in discord channels ... 
    expected_channel_names.append("misc")
    expected_channel_names.append("misc-important")
    expected_channel_names.append("debug")
    expected_channel_names.append("bootlog")
    #expected_channel_names.append("summary")
    
    print(",".join(expected_channel_names))
    # Given channel name,  try create in approproate bot zones. 
    for category_ug_pg in ("UG","PG"):
        for need_important in (True, False):
        
        
            counter = 1
            category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
            category = discord.utils.get(guild.categories, name=category_name)
        
            if not category:
                await guild.create_category(category_name)
                print("Created category"+category_name)
            else:
                print("Fine, category exists"+category_name)
        
            for expected_channel_name in expected_channel_names:
                try:   
                    #print(depts_plus_dict[expected_channel_name], category_ug_pg)
                    if depts_plus_dict[expected_channel_name.upper()[0:4]] == category_ug_pg:
                        if need_important:
                            if "-important" in expected_channel_name:
                                channel = discord.utils.get(guild.text_channels, name=expected_channel_name)
                                category = discord.utils.get(guild.categories, name=category_name)
                                if not channel:
                                    try:
                                        await guild.create_text_channel(expected_channel_name, category=category)
                                        print("Created Channel",expected_channel_name)
                                    except:
                                        counter += 1
                                        category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                                        category = discord.utils.get(guild.categories, name=category_name)
                                    
                                        if not category:
                                            await guild.create_category(category_name)
                                            print("Created category"+category_name)
                                        else:
                                            print("Fine, category exists"+category_name)
                                            
                                        await guild.create_text_channel(expected_channel_name, category=category)
                                        print("Created Channel",expected_channel_name)
                                else:
                                    print("Fine, channel",expected_channel_name,"exists :)")
                        else:
                            channel = discord.utils.get(guild.text_channels, name=expected_channel_name)
                            category = discord.utils.get(guild.categories, name=category_name)
                            if not channel:
                                try:
                                    await guild.create_text_channel(expected_channel_name, category=category)
                                    print("Created Channel",expected_channel_name)
                                except:
                                    counter += 1
                                    category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                                    category = discord.utils.get(guild.categories, name=category_name)
                                
                                    if not category:
                                        await guild.create_category(category_name)
                                        print("Created category"+category_name)
                                    else:
                                        print("Fine, category exists"+category_name)
                                        
                                    await guild.create_text_channel(expected_channel_name, category=category)
                                    print("Created Channel",expected_channel_name)
                            else:
                                print("Fine, channel",expected_channel_name,"exists :)")
                except Exception as e:
                    print(traceback.format_exc())
                    category_name = 'Bot Zone No. {}{}'.format(0, "-misc")
                    category = discord.utils.get(guild.categories, name=category_name)
                    channel = discord.utils.get(guild.text_channels, name=expected_channel_name)
                    category = discord.utils.get(guild.categories, name=category_name)
                    if not channel:
                        await guild.create_text_channel(expected_channel_name, category=category)
                        print("Created Channel",expected_channel_name)
    
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    
    await channel.send('Booting up. ')
    myLoop.start()


                
@tasks.loop(seconds = 60) # repeat after every 10 seconds
async def myLoop():
    try:

        for guild in client.guilds:
            if guild.name == GUILD:
                break
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        allcourses_dict = {}
        try:
            
            debug_write_to_file = False

            endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

            endpoint = requests.head(endpoint, allow_redirects=True).url

            print(endpoint)


            url = endpoint

            page = requests.get(url)

            soup = bs.BeautifulSoup(page.text,'lxml')

            depts = soup.select('.depts')[0]
            depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
            depts_plus_dict = dict(depts_plus)
            depts = depts.get_text("\n").split("\n")
            
            print(depts)
            #os.system("cls")

            

            for dept in (depts):

                url = '{}subject/{}'.format(endpoint, dept)
                
                #url = "http://localhost:8000/{}".format(dept)

                page = requests.get(url)
                
                assert page.status_code == 200
                
                if debug_write_to_file:
                    with open(dept, "w", encoding="utf-8") as rf:
                        rf.write(page.text)

                soup = bs.BeautifulSoup(page.text,'lxml')

                courses = soup.select('#classes > .course')
                
                
                buffered_coursetable_row = []
                
                for course in courses:
                    coursetitle = course.select("h2")[0].decode_contents()
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
                        allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "SECTIONS":coursetable_list_dicts, "FAILURE":"course_table_length_mismatch", "TABLE_COUNT":coursetable_len}
                    else:
                        allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "SECTIONS":coursetable_list_dicts}
                    
                    
                    
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)
            allcourses_dict = {}
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (parsing_all):\n```\n{}\n```\n{}".format(exception_text, e))
            


        #os.system("cls")
        
        
        
        
        notif = {}
        try:
            
            with open("latest_state.json".format(time.time()),"r") as f:
                allcourses_dict_old = json.load(f)

            #pyperclip.copy(output)
            
            if allcourses_dict_old and allcourses_dict:
            
                for diff in list(dictdiffer.diff(allcourses_dict_old, allcourses_dict)):         
                    if not diff[1]:
                        # Adding / deleting from root element, fake things a little. 
                        behaviour = diff[0]
                        for course in diff[2]:
                            os.system("cls")
                            #print(course)
                            
                            ccode, content = course
                            #print(ccode[0:4])
                            #print(notif)
                            #print(notif.get(ccode[0:4], []))
                            notif[ccode[0:4]] = notif.get(ccode[0:4], []) + [(behaviour,ccode,"<AN ENTIRE COURSE>")]
                        continue
                    expected_channel_names_internal = ['CENG', 'CIVL', 'COMP', 'DBAP', 'ECON', 'EESM', 'ELEC', 'ENGG', 'ENTR', 'ENVR', 'EVSM', 'GFIN', 'ISDN', 'ISOM', 'LIFS', 'MAFS', 'MARK', 'MASS', 'MGCS', 'PHYS', 'SBMT', 'SOSC', 'TEMG']
                    for expected_channel_name in expected_channel_names_internal:
                        print(diff, expected_channel_name)
                        if diff[1] and (expected_channel_name in diff[1] or expected_channel_name in diff[1][0]):
                            notif[expected_channel_name] = notif.get(expected_channel_name, []) + [diff]
                            break
                    else: # no break
                        notif["MISC"] = notif.get("MISC", []) + [diff]

                print(notif)
            else:
                raise Exception("Either array is nullish. ")

        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (sending):\n```\n{}\n```\n{}".format(exception_text, e))
            
        try:
            with open("latest_state.json".format(time.time()),"w") as f:
                json.dump(allcourses_dict, f)
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (savedict):\n```\n{}\n```\n{}".format(exception_text, e))
        
        #time.sleep(300)
        try:
            todos = []
            

            
            for importancy, suffix in zip((True,False),("-important","")):
                for k,v in notif.items():
                    try:
                        channel = discord.utils.get(guild.text_channels, name=(k.lower()+suffix))
                        assert channel
                    except:
                        channel = discord.utils.get(guild.text_channels, name="misc"+suffix)
                    for sub_v in v:
                        if importancy == is_important(sub_v) and filter_phantom_change(sub_v):
                            print("```\n{}\n```Check it out on: \n{}".format(preetify_diff(sub_v),check_it_out(sub_v)))
                            todos.append(channel.send("```\n{}\n```Check it out on: \n{}".format(preetify_diff(sub_v),check_it_out(sub_v))))
            print("Begin bang")
            await asyncio.gather(*todos)
            print("End bang")
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (make_messages):\n```\n{}\n```\n{}".format(exception_text, e))
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)
        try:
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (nuclear):\n```\n{}\n```\n{}".format(exception_text, e))
        except:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)
    

    

client.run(TOKEN)