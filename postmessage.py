
from EnhancedDict import *
allcourses_dict_old_forbot = {}




import newdiffer

import quotabeautify

from base64 import b64encode, b64decode

from urllib.parse import urljoin


# bot.py
fake_endpoint = False
import bs4 as bs
import hashlib

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    # https://stackoverflow.com/a/63595341
    
    return b64encode(bytes.fromhex(h.hexdigest())).decode()

import functools

# import grequests

import requests
import os
import sys

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

from tqdm import tqdm
import json   
import pyperclip
import time
import dictdiffer  
import traceback
from datetime import datetime
import asyncio

import os

import discord
from discord import app_commands



from dotenv import load_dotenv

from discord.ext import tasks




import pathlib

latest_state_json_file = str(pathlib.Path(__file__).parent.absolute() / "latest_state.json")

internal_metadata_json_file = str(pathlib.Path(__file__).parent.absolute() / "internal_metadata.json")



user_list_json_file = str(pathlib.Path(__file__).parent.absolute() / "user_list.json")



def get_userlist():
    with open(user_list_json_file, 'r') as f:
        return json.load(f)
    
def save_userlist(usrlist):
    with open(user_list_json_file, 'w') as f:
        json.dump(usrlist, f)


logfile_location = str(pathlib.Path(__file__).parent.absolute() / "logfile.txt")

my_location = str(pathlib.Path(__file__).absolute())

my_hash = sha256sum(my_location)

print(my_hash)

# input()



import asyncio
import concurrent.futures
import requests


import aiohttp

import http3

client_requests = http3.AsyncClient()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))







developer_max_worker_constant = int(os.getenv('DMWC')) # 100 is obsolete. Will cause excessive CPU spikes

developer_use_new_differ = bool(int(os.getenv('DUND'))) # False is the old version. Rollback if all else fails! 

developer_disable_hashchecks = bool(int(os.getenv('DDH')))







bot_identity = "kirito"
client = discord.Client(intents=discord.Intents.default())

tree = app_commands.CommandTree(client)
'''
@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=GUILD_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")'''

async def do_request(method, url):
    '''response = await aiohttp.request(
        method, url, timeout=10
    )'''
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10, ssl=sslcontext) as response:
            return response




def fix_list_locations(location):
    if isinstance(location, list) or isinstance(location, tuple):
        location = ".".join(str(x) for x in location)
    return location



def censor_exception(exception_text):
    return exception_text # unlikely to work on Linux
    base_directory = os.path.expanduser("~")
    base_directory_split = base_directory.split("\\")
    base_directory_split[-1] = "Heathcliff"
    new_base_directory = "\\".join(base_directory_split)
    return exception_text.replace(__file__, "cardinal.py").replace(base_directory, new_base_directory)

def filter_phantom_change(diff):
    event, location, content = diff
    location = fix_list_locations(location)
    if event == "change":
        if isinstance(content[0], str) and isinstance(content[1], str) and content[0].replace("\r","").replace("\n","") == content[1].replace("\r","").replace("\n",""):
            return False
    return True

def preetify_diff(diff):
    event, location, content = diff
    location = fix_list_locations(location)
        
    if ".SECT." in location:
        location = location.replace(".SECT.","-",1)
    formatmode_QEA = False
    try:
        c1, c2 = content
        if quotabeautify.is_dict_QEA(c1) and quotabeautify.is_dict_QEA(c2):
            c1, c2 = quotabeautify.beautify(c1), quotabeautify.beautify(c2)
            
        if quotabeautify.is_string_QEA(c1) and quotabeautify.is_string_QEA(c2):
            formatmode_QEA = True
    except:
        if quotabeautify.is_dict_QEA(content):
            content = quotabeautify.beautify(content)
    
    if event == "add":
        return "\u001b[1;36m[ADD]\u001b[0;37m {}: \n{}".format(location, content)
    elif event == "remove":
        return "\u001b[1;35m[DEL]\u001b[0;37m {}: \n{}".format(location, content)
    elif event == "change":
        if formatmode_QEA:
            return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}".format(location, quotabeautify.diff_between_QEA(quotabeautify.uglify(content[0]), quotabeautify.uglify(content[1])))
        if str(content[0]).isdigit() and str(content[1]).isdigit():
            try:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{} -> {} ({})".format(location, content[0], content[1], "{}{}".format("+" if int(content[1]) > int(content[0]) else "", int(content[1]) - int(content[0])))
            except:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}\nto\n{}".format(location, content[0], content[1])
        elif set((str(content[0]), str(content[1]))) == set(("True", "False")):
            return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{} -> {}".format(location, content[0], content[1])
        else:
            return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}\nto\n{}".format(location, content[0], content[1])
    else:
        return str(diff)
endpoint_ensured = "" 
def check_it_out(diff):
    global endpoint_ensured
    event, location, content = diff
    location = fix_list_locations(location)
    cc = location.split(".")[0]
    url = "{}subject/{}#{}".format(endpoint_ensured, cc[0:4], cc)
    
    fourdigits = endpoint_ensured.split("/")[-2]
    
    # http://evn.asuscomm.com:2280/2230COMP1021
    
    url2 = "http://evn.asuscomm.com:2280/{}{}".format(fourdigits, cc)
    
    return "{}\n{}".format(url2, url)

def get_course_code(diff):
    global endpoint_ensured
    event, location, content = diff
    location = fix_list_locations(location)
    cc = location.split(".")[0]
    return cc
    
def is_important(diff):
    event, location, content = diff
    location = fix_list_locations(location)
    all_unimportant_suffix = (".Wait", ".Enrol", ".Avail")
    for unimportant_strings in all_unimportant_suffix:
        if location.endswith(unimportant_strings): #unimportant_strings in location:
            return (False,)
    if event == "change" and ".QEA." in location:
        c1, c2 = content
        c1 = quotabeautify.uglify(c1)
        c2 = quotabeautify.uglify(c2)
        if c1["Quota"] == c2["Quota"]: # Quota same
            return (False,) #Q same, EA not same, False
        elif c1["Enrol"] == c2["Enrol"] and c1["Avail"] == c2["Avail"]: # EA same
            return (True,) #EA same, Q not same, True
        else:
            return (True,False) # both can
            
    return (True,)
guild_ensured = None
def get_mention_roles(diff):
    global guild_ensured
    #<@&165511591545143296>
    role_type = get_mention_role_type(diff)
    event, location, content = diff
    location = fix_list_locations(location)
    
    if ".SECT." in location:
        location = location.replace(".SECT.","-",1)
    if role_type in ("-traps","-quotas"):
        return "<@&{}>".format(discord.utils.get(guild_ensured.roles, name="{}{}".format(location[0:4], role_type)).id)
    elif not role_type:
        return ""
    else:
        return role_type

        
def get_mention_role_type(diff):
    try:
        event, location, content = diff
        location = fix_list_locations(location)
        
        if ".SECT." in location:
            location = location.replace(".SECT.","-",1)
            
            
        if not "." in location: # new course or del course
            return "-quotas"
        elif event in ("change", "add") and ".QEA." in location and True in is_important(diff): # change or add QEA
            return "-quotas"
        elif ".Instructor" in location: # Change add or remove instructor
            return "-traps"
        else:
            return ""
    except:
        return "Not sure who to @, though. "

channels_to_remove = [str(i).rjust(4, "0") for i in range(60)]
channels_to_remove += [(i+"-important") for i in channels_to_remove]
channels_to_remove = ''''''.splitlines()
channels_to_remove = []

'''
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

'''









def soup_to_allcourses_dict(soup, dept="MISC"):
    allcourses_dict_internal = {}
    courses = soup.select('#classes > .course')
    
    
    buffered_coursetable_row = []
    
    for course in courses:
        course_flags = []
        coursetitle = course.select("h2")[0].decode_contents()
        courseinfo_bar = course.select(".courseinfo > div")
        for elem in courseinfo_bar[:-1]:
            #print(elem.get_text(separator=": "))
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
        quotadetail_info = None
        keys = coursetable.select('tr')[0].select("th")
        keys = [k.text.replace(" & ", "_N_").replace("/","_") for k in keys]
        for row in coursetable.select('tr')[1:]:
            fields = row.select("td")
            
            if buffered_coursetable_row and len(fields) == 4: # is an extension
                '''buffered_coursetable_row_2 = [None for i in range(len(buffered_coursetable_row))]
                buffered_coursetable_row_2 = ["" for i in range(len(buffered_coursetable_row))]
                buffered_coursetable_row_2[1] = "; {}".format(fields[0].get_text(separator="_"))
                buffered_coursetable_row_2[2] = "; {}".format(fields[1].get_text(separator="_"))
                buffered_coursetable_row_2[3] = "; {}".format(fields[2].get_text(separator="_"))'''
                #print(buffered_coursetable_row, buffered_coursetable_row_2)
                '''buffered_coursetable_row = [i if not isinstance(i, str) else str(i)+str(k) for i,k in zip(buffered_coursetable_row, buffered_coursetable_row_2)]'''
                buffered_coursetable_row[1].append(fields[0].get_text(separator="_"))
                buffered_coursetable_row[2].append(fields[1].get_text(separator="_"))
                buffered_coursetable_row[3].append(list(fields[2].stripped_strings)) #MUST LIST
                buffered_coursetable_row[4].append(list(fields[3].stripped_strings)) #MUST LIST
                continue # we are done
            else:
                if buffered_coursetable_row:
                    ### Now get ready to intervene!
                    row_dict_target = dict(zip(keys,buffered_coursetable_row))
                    qea_dict = {}
                    if quotadetail_info is not None:
                        for line in quotadetail_info:
                            student_group, qea_slashed = line.split(": ")
                            qea_split = tuple(int(i) for i in qea_slashed.split("/"))
                            row_dict_target["Quota"] -= qea_split[0]
                            row_dict_target["Enrol"] -= qea_split[1]
                            row_dict_target["Avail"] -= qea_split[2]
                            qea_dict[student_group] = {"Quota": qea_split[0], "Enrol":qea_split[1], "Avail":qea_split[2]}
                    
                    qea_dict["OPEN"] = {"Quota": row_dict_target.pop("Quota"), "Enrol":row_dict_target.pop("Enrol"), "Avail":row_dict_target.pop("Avail")}
                    
                    row_dict_target["QEA"] = qea_dict
                    
                    coursetable_list_dicts.append(row_dict_target)
                    buffered_coursetable_row = []
                    quotadetail_info = None
                if len(buffered_coursetable_row) < len(fields):
                    buffered_coursetable_row = [None for i in range(len(fields))]
                for i, field in enumerate(fields):
                    if field.select("span") and i == 4:
                        buffered_coursetable_row[i] = int(field.select("span")[0].text)
                        # Working column-wise, unwise to process quotadetail here
                        quotadetail_info = tuple(field.select(".quotadetail")[0].stripped_strings)[1:]
                    elif i in (3,4):
                        buffered_coursetable_row[i] = [list(field.stripped_strings)] #MUST LIST
                    elif i in (1,2):
                        buffered_coursetable_row[i] = [field.get_text(separator="_")]
                    elif i in (5,6,7):
                        buffered_coursetable_row[i] = int(field.get_text(separator="_"))
                    elif i in (9,):
                        mkdict = {}
                        if field.select(".popup.consent"):
                            mkdict["consent"] = True
                        else:
                            mkdict["consent"] = False
                        if field.select(".popup.classnotes"):
                            # mkdict["info"] = ''.join(field.select(".popup.classnotes")[0].get_text(separator="; ").splitlines()) # no need newlines here. 
                            mkdict["info"] = list(field.select(".popup.classnotes")[0].stripped_strings) #MUST LIST
                        buffered_coursetable_row[i] = mkdict
                    else: # i in (0,1,2,3,4,5,6,7), or any other
                        buffered_coursetable_row[i] = field.get_text(separator="_")
            #coursetable_list_dicts.append(dict(zip(keys,field2)))
        if buffered_coursetable_row:
            ### Now get ready to intervene!
            row_dict_target = dict(zip(keys,buffered_coursetable_row))
            qea_dict = {}
            if quotadetail_info is not None:
                for line in quotadetail_info:
                    student_group, qea_slashed = line.split(": ")
                    qea_split = tuple(int(i) for i in qea_slashed.split("/"))
                    row_dict_target["Quota"] -= qea_split[0]
                    row_dict_target["Enrol"] -= qea_split[1]
                    row_dict_target["Avail"] -= qea_split[2]
                    qea_dict[student_group] = {"Quota": qea_split[0], "Enrol":qea_split[1], "Avail":qea_split[2]}
            
            qea_dict["OPEN"] = {"Quota": row_dict_target.pop("Quota"), "Enrol":row_dict_target.pop("Enrol"), "Avail":row_dict_target.pop("Avail")}
            
            row_dict_target["QEA"] = qea_dict
            
            coursetable_list_dicts.append(row_dict_target)
            buffered_coursetable_row = []
            quotadetail_info = None
        coursecode = coursetitle.split("-")[0].strip().replace(" ","")
        
        
        if not coursecode:
            coursecode = "{}0871".format(dept)
        
        # print(coursetable_list_dicts)
        sections_keyfield = next(iter(coursetable_list_dicts[0])) #tuple(coursetable_list_dicts[0].keys())[0]
        # next(iter(coursetable_list_dicts[0])) #
        
        
        coursetable_list_dicts_2 = {x.pop(sections_keyfield).replace(" ",""):x for x in coursetable_list_dicts}
        
        if course_table_length_mismatch == True:
            allcourses_dict_internal[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECT":coursetable_list_dicts_2, "_SECTIONS_keyfield": sections_keyfield, "FAILURE":"course_table_length_mismatch", "TABLE_COUNT":coursetable_len}
        else:
            allcourses_dict_internal[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECT":coursetable_list_dicts_2, "_SECTIONS_keyfield": sections_keyfield}
    return allcourses_dict_internal


























## NEWAINCRAD: The crux of the bot's operation
@client.event
async def on_message(message):
    user_list = get_userlist()
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        # It's a private message and not sent by a bot
        user_id = message.author.id

        with open(latest_state_json_file,"r") as f:
            allcourses_subscription = json.load(f)

        message_content = message.content.replace(".", " ").replace(",", " ")
        # Ignore punctuations
        # also who knows what issue will happen if I access message class repeatedly

        lower_message_content = message_content.lower()
        # case insensitive

        words = [x.strip() for x in lower_message_content.split(" ")]

        course = "NULL0871" # can't be too sure that there won't be nullish keys down the line

        for word in words:
            if word.upper() in allcourses_subscription.keys():
                
                course = word.upper()
                break
        
        if course == "NULL0871":
            await message.channel.send(f"Please specify course code, without space. Loaded {len(allcourses_subscription.keys())} courses. ")
            return



        add_or_remove = ""
        
        important = False

        if "important" in words:
            important = True

        everything = False

        if "everything" in words:
            everything = True

        nothing = False

        if "nothing" in words:
            nothing = True

        stats = False

        if "stats" in words:
            stats = True

        if sum([important,everything,nothing,stats]) != 1:
            await message.channel.send("Choose one of important/everything/nothing/stats")
            return

        message_important, message_unimportant = (False, False)

        if important:
            message_important, message_unimportant = (True, False)
        elif everything:
            message_important, message_unimportant = (True, True)
        elif nothing:
            message_important, message_unimportant = (False, False)
        elif stats:
            message_important, message_unimportant = (False, True)

        try:
            user_list[course]
        except:
            user_list[course] = {"I":[], "U":[]}

        try:
            # Check if user_list[course]["I"] is a list
            assert isinstance(user_list[course]["I"], list), "user_list[course]['I'] is not a list"
            # Check if user_list[course]["I"] has append() and remove() methods
            assert hasattr(user_list[course]["I"], "append"), "user_list[course]['I'] does not have an append() method"
            assert hasattr(user_list[course]["I"], "remove"), "user_list[course]['I'] does not have a remove() method"
        except:
            user_list[course]["I"] = []
        
        try:
            # Check if user_list[course]["U"] is a list
            assert isinstance(user_list[course]["U"], list), "user_list[course]['U'] is not a list"
            # Check if user_list[course]["U"] has append() and remove() methods
            assert hasattr(user_list[course]["U"], "append"), "user_list[course]['U'] does not have an append() method"
            assert hasattr(user_list[course]["U"], "remove"), "user_list[course]['U'] does not have a remove() method"
        except:
            user_list[course]["U"] = []

        if message_important:
            user_list[course]["I"].append(user_id)
        else:
            try:
                user_list[course]["I"].remove(user_id)
            except:
                pass

        user_list[course]["I"] = list(set(user_list[course]["I"]))

        if message_unimportant:
            user_list[course]["U"].append(user_id)
        else:
            try:
                user_list[course]["U"].remove(user_id)
            except:
                pass

        user_list[course]["U"] = list(set(user_list[course]["U"]))


        
        print(user_list)
        save_userlist(user_list)
        await message.channel.send("Your command had worked. ")


        # Notification types: [None], [Important], [Noise], [Everything]
        # Add important, Add everything, remove everything




        ## NEWINCRAD: I HOPE THIS WORKS




@client.event
async def on_ready():

    # await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Ready!")
    global channels_to_remove
    global guild_ensured
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            
            guild_ensured = guild
            break
    else:
        print("GUILD NOT FOUND!!!")
        input()
            
    print(guild.features)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
    category_name = 'Bot Zone No. {}{}'.format(0, "-misc")
    category = discord.utils.get(guild.categories, name=category_name)

    if not category:
        await guild.create_category(category_name)
        print("Created category"+category_name)
        category = discord.utils.get(guild.categories, name=category_name)
    else:
        print("Fine, category exists "+category_name)
    
    for important_preboot_channels in ("debug", "bootlog", "updates", "battle-report", "battle-report-fallback"):
        channel = discord.utils.get(guild.text_channels, name=important_preboot_channels)
        if not channel:
            try:
                channel = await guild.create_text_channel(important_preboot_channels, category=category)
                # await channel.edit(type=discord.ChannelType.news)
                print(channel.type)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                await guild.create_text_channel(important_preboot_channels)
                
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    
    await channel.send('Waking up. ')
    #embed=discord.Embed(title="Battle report", description="```ansi\n{}\n```See: {}", color=0x00ffff)
    # #embed.set_footer(text="")
    #await channel.send(embed=embed)
    #input()
    
    for channel_name in channels_to_remove:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if channel:
            try:
                print("Removing channel",channel_name)
                await channel.delete()
            except:
                print("Not found channel",channel_name)
    channels_to_remove = []
    try:
        debug_write_to_file = False

        endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

        endpoint = requests.head(endpoint, allow_redirects=True).url

        print(endpoint)
        if fake_endpoint:
            endpoint = 'http://localhost:8000/'
        url = endpoint

        page = requests.get(url)

        soup = bs.BeautifulSoup(page.text,'lxml')

        depts = soup.select('.depts')[0]
        
        depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
        depts_plus_dict = dict(depts_plus)
        depts = depts.get_text("\n").split("\n")
        
        expected_channel_names = depts
        expected_channel_names_internal = tuple(depts)
        print("ecni",expected_channel_names_internal)
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

    # NEWAINCRAD: we want none of the subjects but we want all of the bot zone 0 channels
    expected_channel_names = []
    expected_channel_names.append("misc")
    expected_channel_names.append("misc-important")
    expected_channel_names.append("updates")
    expected_channel_names.append("debug")
    
    # expected_channel_names.append("tocreate")
    
    expected_channel_names.append("bootlog")
    expected_channel_names.append("hkust-server-error")
    expected_channel_names.append("hashes-{}".format(bot_identity))
    
    
    
    
    '''teststring = "able"
    expected_channel_names.append(teststring)
    depts_plus_dict[teststring] = "PG"'''
    #expected_channel_names.append("summary")
    
    print(",".join(expected_channel_names))
    
    # NEWAINCRAD: We create those channels
    for important_preboot_channels in expected_channel_names:
        channel = discord.utils.get(guild.text_channels, name=important_preboot_channels)
        if not channel:
            try:
                channel = await guild.create_text_channel(important_preboot_channels, category=category)
                # await channel.edit(type=discord.ChannelType.news)
                print(channel.type)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                await guild.create_text_channel(important_preboot_channels)

    # Given channel name,  try create in approproate bot zones. 


    ## NEWAINCRAD: We no longer need to create any channels pre-boot



    """for category_ug_pg in ("UG","PG"):
        for need_important in (True, False):
        
        
            counter = 1
            category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
            category = discord.utils.get(guild.categories, name=category_name)
        
            if not category:
                await guild.create_category(category_name)
                print("Created category"+category_name)
            else:
                print("Fine, category exists "+category_name)
        
            for expected_channel_name in expected_channel_names:
                try:   
                    #print(depts_plus_dict[expected_channel_name], category_ug_pg)
                    if len(expected_channel_name) != 4:
                        raise Exception("Handle by misc")
                    if len(expected_channel_name.split("-")[0]) == 4 and expected_channel_name.split("-")[0] != "misc" and depts_plus_dict[expected_channel_name.upper()[0:4]] == category_ug_pg:
                        if need_important:
                            if "-important" in expected_channel_name:
                                channel = discord.utils.get(guild.text_channels, name=expected_channel_name)
                                category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                                category = discord.utils.get(guild.categories, name=category_name)
                                if not channel:
                                    try:
                                        await guild.create_text_channel(expected_channel_name, category=category)
                                        print("Created Channel",expected_channel_name)
                                    except:
                                        proceed = True
                                        while proceed and counter < 10:
                                            try:
                                                counter += 1
                                                category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                                                category = discord.utils.get(guild.categories, name=category_name)
                                            
                                                if not category:
                                                    await guild.create_category(category_name)
                                                    print("Created category"+category_name)
                                                    category = discord.utils.get(guild.categories, name=category_name)
                                                else:
                                                    print("Fine, category exists "+category_name)
                                                    
                                                await guild.create_text_channel(expected_channel_name, category=category)
                                                print("Created Channel",expected_channel_name)
                                                proceed = False
                                            except:
                                                pass
                                else:
                                    print("Fine, channel",expected_channel_name,"exists :)")
                        else:
                            channel = discord.utils.get(guild.text_channels, name=expected_channel_name)
                            category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                            category = discord.utils.get(guild.categories, name=category_name)
                            if not channel:
                                try:
                                    await guild.create_text_channel(expected_channel_name, category=category)
                                    print("Created Channel",expected_channel_name)
                                except:
                                    proceed = True
                                    while proceed and counter < 10:
                                        try:
                                            counter += 1
                                            category_name = '{} Bot Zone No. {}{}'.format(category_ug_pg, counter, "-important" if need_important else "")
                                            category = discord.utils.get(guild.categories, name=category_name)
                                        
                                            if not category:
                                                await guild.create_category(category_name)
                                                print("Created category"+category_name)
                                                category = discord.utils.get(guild.categories, name=category_name)
                                            else:
                                                print("Fine, category exists "+category_name)
                                                
                                            await guild.create_text_channel(expected_channel_name, category=category)
                                            print("Created Channel",expected_channel_name)
                                            proceed = False
                                        except:
                                            pass
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
                    else:
                        print("Fine, channel",expected_channel_name,"exists :)")
    
"""
    
    ### THE FOLLOWING DOESN'T WORK BECAUSE API NOT PRESENT
    '''for category in guild.categories:
        
        if "Bot Zone" in category.name:
            print("Sorting",category.name)
            channel_names_unsorted = list(channel.name for channel in category.channels)
            pos_list = (list(channel.position for channel in category.channels))
            print(pos_list)
            themin = min(list(channel.position for channel in category.channels))
            channel_names = sorted(channel_names_unsorted)
            
            
            
            
            
            
            
            
            if not channel_names_unsorted == channel_names:
                channel = discord.utils.get(guild.text_channels, name="bootlog")
                await channel.send('Sorting {}, please wait...'.format(category.name))
                channel_names_unsorted_ordinal = [channel_names.index(x) for x in channel_names_unsorted]
                print("---ACTION---")
                print(channel_names_unsorted_ordinal)
                moves = testing(channel_names_unsorted_ordinal)
                print(moves)
                print("------------")
                for move in moves:
                    m1, m2 = move
                    print(channel_names[m1], pos_list[int(m2-1+themin)])
                    print(discord.utils.get(category.channels, name=channel_names[m1]).position)
                    await discord.utils.get(category.channels, name=channel_names[m1]).edit(position=pos_list[int(m2-1+themin)])
                    
                    print(discord.utils.get(category.channels, name=channel_names[m1]).position)
                pos_list = (list(channel.position for channel in category.channels))
                print(pos_list)
                channel_names_unsorted = list(channel.name for channel in category.channels)
                channel_names = sorted(channel_names_unsorted)
                print(channel_names_unsorted)
                channel_names_unsorted_ordinal = [channel_names.index(x) for x in channel_names_unsorted]
                print(channel_names_unsorted_ordinal)

            else:
                print("Doesn't need sorting",category.name)'''
    
    ## NEWAINCRAD: some issues with auto-sort. We dont need sorting for single bot zone anyways. 
    """for category in guild.categories:
        
        if "Bot Zone" in category.name:
            print("Sorting",category.name)
            channel_names_unsorted = list(channel.name for channel in category.channels)
            channel_names = sorted(channel_names_unsorted)
            
            if not channel_names_unsorted == channel_names:
                
                channel = discord.utils.get(guild.text_channels, name="bootlog")
                await channel.send('Sorting {}, \nplease wait...'.format(category.name))
                
                print("Needs sorting",category.name)
                for channel_name in channel_names:
                    print(channel_name)
                    await discord.utils.get(category.channels, name=channel_name).edit(position=channel_names.index(channel_name))
                    print(channel_name, channel_names.index(channel_name))"""
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    
    for category in guild.categories:
        if "Bot Zone" in category.name:
            count = 0
            for channel in category.channels:
                if channel.type != discord.ChannelType.text and "battle-report" not in channel.name:
                    count += 1
            if count:
                channel = discord.utils.get(guild.text_channels, name="bootlog")
                await channel.send('Converting {} channel{} to text\nin {}, please wait...'.format(count, "" if count == 1 else "s", category.name))
                for channel in category.channels:
                    if channel.type != discord.ChannelType.text and "battle-report" not in channel.name:
                        await channel.edit(type=discord.ChannelType.text)
                        
    for typename in ("-traps", "-quotas"):
        for deptname in expected_channel_names_internal:
            tgtname = deptname+typename
            role = discord.utils.get(guild.roles, name=tgtname)
            if not role:
                await guild.create_role(name=tgtname)
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    await channel.send("Alright. Let's fight!")
    
    
    myLoop.start()

# last_valid_endpoint is endpoint_ensured
last_parsed_url = None
last_parsed_dept = None
@tasks.loop(seconds = 90) # repeat after every 10 seconds
async def myLoop():
    global last_parsed_url
    global last_parsed_dept
    global endpoint_ensured
    try:

        for guild in client.guilds:
            if guild.id == GUILD_ID:
                break
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        
        allcourses_dict = {}
        try:
            
            debug_write_to_file = False
            if last_parsed_url and last_parsed_dept:
                # use newer endpoint determination and course list determination. 
                # iterate through course list until get a fresh page
                # then go on
                print("---REVO - FLASHBACK---")
                
                endpoint = last_parsed_url
                endpoint_ensured = last_parsed_url
                print(endpoint)
                
                depts = last_parsed_dept
                
                print(depts)
                
                for dept in depts:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                        loop = asyncio.get_event_loop()
                        futures = [

                            loop.run_in_executor(
                                executor, 
                                functools.partial(requests.get, url=target_url, timeout= 10)
                            )
                            for target_url in ["{}subject/{}".format(endpoint, dept)]
                        ]
                        rs2 = await asyncio.gather(*futures)
                    if rs2[0].status_code == 200:
                        break
                
                # rs2[0] should be what it wants
                
                    
                
            else:    
                endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    loop = asyncio.get_event_loop()
                    futures = [

                        loop.run_in_executor(
                            executor, 
                            functools.partial(requests.head, url=target_url, allow_redirects=True, timeout= 10)
                        )
                        for target_url in [endpoint]
                    ]
                    rs2 = await asyncio.gather(*futures)

                endpoint = rs2[0]

                if endpoint.status_code != 200:
                    if endpoint.status_code in (500, 404) and endpoint_ensured:
                        channel = discord.utils.get(guild.text_channels, name="hkust-ignored-error")
                        await channel.send("Status code {}, ignored".format(endpoint.status_code))
                        endpoint = endpoint_ensured
                    else:
                        raise Exception(endpoint.status_code)

                # endpoint = requests.head(endpoint, allow_redirects=True, timeout=10)
                
                # assert endpoint.status_code == 200
                
                endpoint = endpoint.url
                endpoint_ensured = endpoint
                
                if fake_endpoint:
                    endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/2210/'
                print(endpoint)


                url = endpoint
                
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    loop = asyncio.get_event_loop()
                    futures = [

                        loop.run_in_executor(
                            executor, 
                            functools.partial(requests.get, url=target_url, timeout= 10)
                        )
                        for target_url in [url]
                    ]
                    rs2 = await asyncio.gather(*futures)
                    
                    
                    
                    
                    
                    
                #channel = discord.utils.get(guild.text_channels, name="hkust-server-error")
                #await channel.send("Status code 500")
                
                
                
                
            
            
            page = rs2[0]
            # page = requests.get(url, timeout=10)
            if page.status_code != 200:
                if page.status_code == 500:
                    channel = discord.utils.get(guild.text_channels, name="hkust-server-error")
                    await channel.send("Status code 500")
                    return
                else:
                    raise Exception(page.status_code)
            assert page.status_code == 200
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                loop = asyncio.get_event_loop()
                futures = [

                    loop.run_in_executor(
                        executor, 
                        bs.BeautifulSoup, 
                        ptxt, 
                        'lxml'
                    )
                    for ptxt in [page.text]
                ]
                rs2_beautifulsoup = await asyncio.gather(*futures)
            soup = rs2_beautifulsoup[0]
            #soup = bs.BeautifulSoup(page.text,'lxml')

            depts = soup.select('.depts')[0]
            
            depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
            depts_plus_dict = dict(depts_plus)
            
            expected_channel_names_internal = depts_plus_dict.keys()
            depts = depts.get_text("\n").split("\n")
            
            print(depts)
            # clear_console()
            
            try:
                os.mkdir(str(pathlib.Path(__file__).parent.absolute() / "filestore"))
            except:
                pass
                
            fourdigits = endpoint_ensured.split("/")[-2]
            
            print(fourdigits)
            
            try:
                os.mkdir(str(pathlib.Path(__file__).parent.absolute() / "filestore/{}".format(fourdigits)))
            except:
                pass
            
            
            
            urls = ['{}subject/{}'.format(endpoint, dept) for dept in depts]
            
            
            def url_to_state_purl_allcourses_dict(url):
                state = None
                purl = None
                depts = None
                allcourses_dict = None
                
                req = requests.get(url=url, timeout= 10)
                state = req.status_code
                fourdigits = url.split("/")[-3]
                dept = url.split("/")[-1]
                try:
                    fourdigits = url.split("/")[-3]
                    dept = url.split("/")[-1]
                    with open(str(pathlib.Path(__file__).parent.absolute() / "filestore/{}/{}.html".format(fourdigits, dept)), "w", encoding="utf-8") as savefile:
                        savefile.write(req.text)
                except:
                    pass
                if state == 200:
                
                    soup = bs.BeautifulSoup(req.text,'lxml')
                    purl = urljoin(url, soup.select(".termselect > a")[0]['href'])
                    allcourses_dict = soup_to_allcourses_dict(soup, dept=dept)
                    depts = soup.select('.depts')[0].get_text("\n").split("\n")
                    return (state, purl, depts, allcourses_dict)
                else:
                    return (state, purl, depts, allcourses_dict)
                    
            with concurrent.futures.ThreadPoolExecutor(max_workers=developer_max_worker_constant) as executor:
                loop = asyncio.get_event_loop()
                futures = [
                    loop.run_in_executor(
                        executor, 
                        url_to_state_purl_allcourses_dict, 
                        target_url
                    )

                    for target_url in urls
                ]
                rs_ultimate = await asyncio.gather(*futures)
            
            """
            print("getting all pages")
            with concurrent.futures.ThreadPoolExecutor(max_workers=developer_max_worker_constant) as executor:
                loop = asyncio.get_event_loop()
                futures = [

                    loop.run_in_executor(
                        executor, 
                        functools.partial(requests.get, url=target_url, timeout= 10)
                    )
                    for target_url in urls
                ]
                rs2 = await asyncio.gather(*futures)
            print("got all pages")

            print(depts)
            
            
            for page in rs2:
                if page.status_code == 200:
                    last_valid_page = page

            """
            try:
                for typename in ("-traps", "-quotas"):
                    for deptname in depts:
                        tgtname = deptname+typename
                        role = discord.utils.get(guild.roles, name=tgtname)
                        if not role:
                            channel = discord.utils.get(guild.text_channels, name="bootlog")
                            await channel.send("Creating role {} mid-battle".format(deptname))
                            await guild.create_role(name=tgtname)
            except:
                channel = discord.utils.get(guild.text_channels, name="bootlog")
                await channel.send("Can't create role {}".format(deptname))
            """
            for i, dept in enumerate(tqdm(depts)):
                
                page = rs2[i]

                try:
                    with open(str(pathlib.Path(__file__).parent.absolute() / "filestore/{}/{}.html".format(fourdigits, dept)), "w", encoding="utf-8") as savefile:
                        savefile.write(page.text)
                except:
                    pass
                if page.status_code != 200:
                    if page.status_code == 500:
                        channel = discord.utils.get(guild.text_channels, name="hkust-server-error")
                        await channel.send("Status code 500")
                        return
                    else:
                        raise Exception(page.status_code)
                
                assert page.status_code == 200
                
                if debug_write_to_file:
                    with open(dept, "w", encoding="utf-8") as rf:
                        rf.write(page.text)
                        
                #print("Parsing",dept)
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    loop = asyncio.get_event_loop()
                    futures = [

                        loop.run_in_executor(
                            executor, 
                            bs.BeautifulSoup, 
                            ptxt, 
                            'lxml'
                        )
                        for ptxt in [page.text]
                    ]
                    rs2_beautifulsoup = await asyncio.gather(*futures)
                #print("Parsed",dept)
                # soup = rs2_beautifulsoup[0]
                #soup = bs.BeautifulSoup(page.text,'lxml')
                allcourses_dict.update(soup_to_allcourses_dict(rs2_beautifulsoup[0]))
                """
            for state, purl, dept, allcourses_dict_partial in rs_ultimate:
                if state != 200:
                    raise Exception("HTML state {}".format(state))
                last_parsed_url = purl
                last_parsed_dept = dept
                allcourses_dict.update(allcourses_dict_partial)
                
                
                
                
                    
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)
            allcourses_dict = {}
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (parsing_all):\n```\n{}\n```\n{}".format(exception_text, e))
            


        # clear_console()
        
        
        
        notif = {}

        
        
        try:
            
            with open(latest_state_json_file,"r") as f:
                allcourses_dict_old = json.load(f)
            #pyperclip.copy(output)
            
            if allcourses_dict_old and allcourses_dict:
                if developer_use_new_differ:
                    the_diffs = newdiffer.diff2(allcourses_dict_old, allcourses_dict)
                else:
                    the_diffs = tuple(dictdiffer.diff(allcourses_dict_old, allcourses_dict))
                for diff in the_diffs: 
                    if "." not in diff[1].replace(".SECT.","-"): # and diff[1][4:8].isdigit(): ## just a course 
                        diff = list(diff)
                        diff[2] = "<AN ENTIRE {}>".format("COURSE" if "." not in diff[1] else "SECTION")
                    if not diff[1]:
                        '''with open("logfile.txt", "a") as lf:
                            lf.writelines(["###MISC-IMPORTANT###", str(diff), datetime.now().strftime("%H:%M:%S"), "------"])
                            channel = discord.utils.get(guild.text_channels, name="debug")
                            await channel.send("check logfile.txt to debug strange misc-important NOW!")'''
                        # Adding / deleting from root element, fake things a little. 
                        behaviour = diff[0]
                        for course in diff[2]:
                            # clear_console()
                            #print(course)
                            
                            ccode, content = course
                            #print(ccode[0:4])
                            #print(notif)
                            #print(notif.get(ccode[0:4], []))
                            if len(ccode[0:4])==4:
                                notif[ccode[0:4]] = notif.get(ccode[0:4], []) + [(behaviour,ccode,"<AN ENTIRE COURSE (LEGACY)>")]
                            else:
                                notif["MISC"] = notif.get("MISC", []) + [(behaviour,ccode,str(content)[0:1000])]
                        continue
                    #expected_channel_names_internal = ['CENG', 'CIVL', 'COMP', 'DBAP', 'ECON', 'EESM', 'ELEC', 'ENGG', 'ENTR', 'ENVR', 'EVSM', 'GFIN', 'ISDN', 'ISOM', 'LIFS', 'MAFS', 'MARK', 'MASS', 'MGCS', 'PHYS', 'SBMT', 'SOSC', 'TEMG']
                    for expected_channel_name in expected_channel_names_internal:
                        print(diff, expected_channel_name)
                        if diff[1] and (diff[1].startswith(expected_channel_name) or diff[1][0].startswith(expected_channel_name)):
                            notif[expected_channel_name] = notif.get(expected_channel_name, []) + [diff]
                            break
                    else: # no break
                        notif["MISC"] = notif.get("MISC", []) + [diff]

                #print(notif)
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
            if allcourses_dict:
                with open(latest_state_json_file,"w") as f:
                    json.dump(allcourses_dict, f)
                json_hash = "`{}`".format(sha256sum(latest_state_json_file))
                print(json_hash)
                channel = discord.utils.get(guild.text_channels, name="hashes-{}".format(bot_identity))
                messages = [message async for message in channel.history(limit=1)]
                if not messages:
                    await channel.send(json_hash)
                else:
                    try:
                        if messages[0].content != json_hash:
                            await messages[0].edit(content=json_hash)
                    except:
                        await channel.send(json_hash)
                #await channel.send(json_hash)
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (savedict):\n```\n{}\n```\n{}".format(exception_text, e))
            
        metadata = {"HKUST Server Endpoint": endpoint_ensured, "CQO (SHA256-Base64)": my_hash}
        ignore_updates = False
        try:
            with open(internal_metadata_json_file, "r") as f:
                metadata_old = json.load(f)
            
            
            if metadata and metadata_old:
                for diff in dictdiffer.diff(metadata_old, metadata):# list(dictdiffer.diff(metadata_old, metadata)):
                    ignore_updates = not developer_disable_hashchecks
                    '''_, area, change = diff
                    channel = discord.utils.get(guild.text_channels, name="updates")
                    await channel.send("```\nUpdated {} from:\n{}\nto\n{}\n```{}\n_ _".format(area, change[0], change[1], "As such, {} notification{} {} safely ignored. ".format(len(notif), "" if len(notif) == 1 else "s", "is" if len(notif) == 1 else "are") if notif else "Doesn't matter, no notifications anyways. "))
                    if not developer_disable_hashchecks:
                        del notif
                        notif = {}'''
            else:
                raise Exception("Either metadata is nullish. ")
        
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (loadmeta):\n```\n{}\n```\n{}".format(exception_text, e))
        
        #time.sleep(300)

        ## NEWAINCRAD: no longer need to populate todos in the old way, since todos are just channel-directed messages.

        ## NEWAINCRAD: We may still need notifs, that's the entire point. 
        """try:
            todos = []
            ignore_updates_count = 0
            
            
            for importancy, suffix in zip((True,False),("-important","")):
                for k,v in notif.items():
                    try:
                        channel = discord.utils.get(guild.text_channels, name=(k.lower()+suffix))
                        assert channel
                    except:
                        # create channel
                        
                        try:
                            counter = 1
                            depts_plus_dict[k]
                            category_name = '{} Bot Zone No. {}{}'.format(depts_plus_dict[k], counter, "-important" if importancy else "")
                            category = discord.utils.get(guild.categories, name=category_name)
                            proceed = True
                            while proceed and counter < 10:
                                try:
                                    if not category:
                                        await guild.create_category(category_name)
                                    category = discord.utils.get(guild.categories, name=category_name)
                                    await guild.create_text_channel((k.lower()+suffix), category=category)
                                    channel = discord.utils.get(guild.text_channels, name=(k.lower()+suffix))
                                    proceed=False
                                except:
                                    # it is full
                                    counter += 1
                                    category_name = '{} Bot Zone No. {}{}'.format(depts_plus_dict[k], counter, "-important" if importancy else "")
                                    category = discord.utils.get(guild.categories, name=category_name)
                                    if not category:
                                        await guild.create_category(category_name)
                                    category = discord.utils.get(guild.categories, name=category_name)
                            if proceed:
                                channel = discord.utils.get(guild.text_channels, name="misc"+suffix)
                        except:
                            channel = discord.utils.get(guild.text_channels, name="misc"+suffix)
                    for sub_v in v:
                        if importancy in is_important(sub_v) and filter_phantom_change(sub_v):
                            if not ignore_updates:
                                sending_string = "```ansi\n{}\n```See: {}\n{}_ _".format(preetify_diff(sub_v),check_it_out(sub_v), get_mention_roles(sub_v))
                                ## Added ANSI formatting here
                                print(sending_string)
                                if len(sending_string) < 1900:
                                    todos.append(channel.send(sending_string))
                                else:
                                    with open(logfile_location, "a", encoding="utf-8") as lf:
                                        lf.writelines(["###TOO-LONG-STRING###", sending_string, datetime.now().strftime("%H:%M:%S"), "------"])
                                        channel = discord.utils.get(guild.text_channels, name="debug")
                                        await channel.send("check logfile.txt to debug exceed 2000 characters NOW!")
                            
                            ignore_updates_count += 1
            print("Begin bang")
            olddt = datetime.now().strftime("%H:%M:%S")
            print(olddt)
            

            await asyncio.gather(*todos)
            print("End bang")
            print(olddt, datetime.now().strftime("%H:%M:%S"))
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (make_messages):\n```\n{}\n```\n{}".format(exception_text, e))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{}'s data".format(datetime.now().strftime("%H:%M:%S"))))"""


        # NEWAINCRAD: Rework todos generation for private messages

        try:
            todos = []
            ignore_updates_count = 0
            
            
            # suffix don't matter anymore
            # for importancy, suffix in zip((True,False),("-important","")):
            clear_console()
            print("Notif")
            print(notif)
            print("-----")
            print("Begin send")
            for importancy in (True, False):
                for k,v in notif.items():
                    # channel creation has been removed entirely. 
                    for sub_v in v:
                        if importancy in is_important(sub_v) and filter_phantom_change(sub_v):
                            if not ignore_updates:
                                sending_string = "```ansi\n{}\n```See: {}\n{}_ _".format(preetify_diff(sub_v),check_it_out(sub_v), get_mention_roles(sub_v))
                                ## Added ANSI formatting here
                                print(sending_string)


                                if len(sending_string) < 1900:
                                    # todos.append(channel.send(sending_string))
                                    course_code = get_course_code(sub_v)
                                    letter = ""
                                    if importancy:
                                        letter = "I"
                                    else:
                                        letter = "U"
                                    user_list = get_userlist()
                                    for user_id in user_list[course_code][letter]:
                                        user = await client.fetch_user(user_id)
                                        if user is None:
                                            print(f'User {user} not found.')
                                            continue
                                        try:
                                            await user.send(sending_string)
                                            await asyncio.sleep(1)
                                            print('Private message sent.')
                                        except discord.Forbidden:
                                            print('Unable to send a private message to that user.')
                                else:
                                    with open(logfile_location, "a", encoding="utf-8") as lf:
                                        lf.writelines(["###TOO-LONG-STRING###", sending_string, datetime.now().strftime("%H:%M:%S"), "------"])
                                        channel = discord.utils.get(guild.text_channels, name="debug")
                                        await channel.send("check logfile.txt to debug exceed 2000 characters NOW!")
                            
                            ignore_updates_count += 1 # this just a counter that always increments. 
            print("Begin bang")
            olddt = datetime.now().strftime("%H:%M:%S")
            print(olddt)
            

            await asyncio.gather(*todos)
            print("End bang")
            print(olddt, datetime.now().strftime("%H:%M:%S"))
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (make_messages):\n```\n{}\n```\n{}".format(exception_text, e))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{}'s data".format(datetime.now().strftime("%H:%M:%S"))))
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
    try:
        notif
        assert ignore_updates != True
    except:
        notif = {} #make the code below give up
    '''
    try:
        if notif:
            outstr_battle_report = []
            notif_2 = dict(sorted(notif.items()))
            for k,v in notif_2.items():
                count_of_quotas = len(list("COUNT" for sub_v in v if get_mention_role_type(sub_v) == "-quotas"))
                count_of_traps = len(list("COUNT" for sub_v in v if get_mention_role_type(sub_v) == "-traps"))
                outstr_battle_report.append("{}: {} update{}{}{}".format(k.upper(), len(v), "" if len(v)==1 else "s", ", \u001b[0;36mQUOTAS:{}\u001b[0;37m".format(count_of_quotas) if count_of_quotas else "", ", \u001b[0;35mTRAPS:{}\u001b[0;37m".format(count_of_traps) if count_of_traps else ""))
                
            outstr_battle_report = "\n".join(outstr_battle_report)
            print(outstr_battle_report)
            if outstr_battle_report:
                try:
                    channel = discord.utils.get(guild.text_channels, name="battle-report")
                    msg = await channel.send("```ansi\n\u001b[0;37m{}\n```".format(outstr_battle_report))
                    try:
                        await msg.publish()
                    except:
                        pass
                except:
                    channel = discord.utils.get(guild.text_channels, name="battle-report-fallback")
                    await channel.send("```ansi\n\u001b[0;37m{}\n```".format(outstr_battle_report))
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)
        try:
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (battle-report):\n```\n{}\n```\n{}".format(exception_text, e))
        except:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)
            
    '''  
    try:
        if notif:
            outstr_battle_report = []
            #print(notif)
            notif_2 = notif.values()
            #print(notif_2)
            notif_2 = [item for sublist in notif_2 for item in sublist] # Flatten, see https://stackoverflow.com/a/952952
            notif_2 = [tuple(x) for x in notif_2]
            try:
                notif_2.sort()
            except:
                print(notif_2)
            
            #print(notif_2)
            course_updates = {} # normal (unused), quotas, traps
            course_updates_2 = {} # normal only
            for each_notif in notif_2:
                event, location, content = each_notif
                location = fix_list_locations(location)
                course = location.split(".")[0]
                
                
                if get_mention_role_type(each_notif) == "-traps":
                    old_list = course_updates.get(course, [0,0,0])
                    old_list[2] += 1
                    course_updates[course] = old_list
                elif get_mention_role_type(each_notif) == "-quotas":
                    old_list = course_updates.get(course, [0,0,0])
                    old_list[1] += 1
                    course_updates[course] = old_list
                else:
                    old_list_2 = course_updates_2.get(course[0:4], [0])
                    old_list_2[0] += 1
                    course_updates_2[course[0:4]] = old_list_2
                
                
            course_updates = {k: v for k, v in sorted(course_updates.items(), key=lambda item: item[0])}
            course_updates_2 = {k: v for k, v in sorted(course_updates_2.items(), key=lambda item: item[0])}
            for course, ntq in course_updates.items():
                outstr_battle_report.append(
                    #"{}: {} update{}{}{}{}".format(
                    "{}: {}{}{}".format(
                        course.ljust(9," "),
                        #ntq[0],
                        #"" if ntq[0] == 1 else "s",
                        "\u001b[0;36mQUOTA:{} ".format(ntq[1]) if ntq[1] else "",
                        "\u001b[0;35mTRAPS:{} ".format(ntq[2]) if ntq[2] else "",
                        "\u001b[0;37m" if (ntq[1] or ntq[2]) else "",
                    )
                )
            for course, ntq in course_updates_2.items():
                outstr_battle_report.append(
                    #"{}: {} update{}{}{}{}".format(
                    "{}: {} update{}".format(
                        course,
                        ntq[0],
                        "" if ntq[0] == 1 else "s",
                        #", \u001b[0;36mQUOTAS:{}".format(ntq[1]) if ntq[1] else "",
                        #", \u001b[0;35mTRAPS:{}".format(ntq[2]) if ntq[2] else "",
                        #"\u001b[0;37m" if (ntq[1] or ntq[2]) else "",
                    )
                )

                
            outstr_battle_report = "\n".join(outstr_battle_report)
            # clear_console()
            print(outstr_battle_report)
            
            if outstr_battle_report:
                try:
                    assert len(outstr_battle_report) < 4095
                    channel = discord.utils.get(guild.text_channels, name="battle-report")
                    embed=discord.Embed(title="Battle report", description="```ansi\n\u001b[0;37m{}\n```See: {}".format(outstr_battle_report, endpoint_ensured), color=0x00ffff)
                    # embed.set_footer(text="")
                    msg = await channel.send(embed=embed)
                    try:
                        assert channel.type == discord.ChannelType.news
                        await msg.publish()
                    except:
                        pass
                except:
                    try:
                        channel = discord.utils.get(guild.text_channels, name="battle-report")
                        msg = await channel.send("Too many changes to document. Check CQO yourself".format(outstr_battle_report))
                        try:
                            assert channel.type == discord.ChannelType.news
                            await msg.publish()
                        except:
                            pass
                    except:
                        channel = discord.utils.get(guild.text_channels, name="battle-report-fallback")
                        msg = await channel.send("Too many changes to document AND rate-limit reached. Check CQO yourself".format(outstr_battle_report))
                        try:
                            assert channel.type == discord.ChannelType.news
                            await msg.publish()
                        except:
                            pass
                '''try:
                    channel = discord.utils.get(guild.text_channels, name="battle-report")
                    msg = await channel.send("```ansi\n\u001b[0;37m{}\n```".format(outstr_battle_report))
                    try:
                        await msg.publish()
                    except:
                        pass
                except:
                    channel = discord.utils.get(guild.text_channels, name="battle-report-fallback")
                    await channel.send("```ansi\n\u001b[0;37m{}\n```".format(outstr_battle_report))'''
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)
        try:
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (battle-report):\n```\n{}\n```\n{}".format(exception_text, e))
        except:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)
        
        
    metadata = {"HKUST Server Endpoint": endpoint_ensured, "CQO (SHA256-Base64)": my_hash}
    try:
        with open(internal_metadata_json_file, "r") as f:
            metadata_old = json.load(f)
        
        
        if metadata and metadata_old:
            for diff in dictdiffer.diff(metadata_old, metadata):# list(dictdiffer.diff(metadata_old, metadata)):
                ignore_updates = not developer_disable_hashchecks
                _, area, change = diff
                channel = discord.utils.get(guild.text_channels, name="updates")
                try:
                    ignore_updates_count
                    await channel.send("```\nUpdated {} from:\n{}\nto\n{}\n```{}\n_ _".format(area, change[0], change[1], "As such, {} notification{} {} safely ignored. ".format(ignore_updates_count, "" if ignore_updates_count == 1 else "s", "is" if ignore_updates_count == 1 else "are") if ignore_updates_count else "Doesn't matter, no notifications anyways. "))
                except:
                    pass
        else:
            raise Exception("Either metadata is nullish. ")
    
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)

        channel = discord.utils.get(guild.text_channels, name="debug")
        await channel.send("admin pls help (loadmeta):\n```\n{}\n```\n{}".format(exception_text, e))


    metadata = {"HKUST Server Endpoint": endpoint_ensured, "CQO (SHA256-Base64)": my_hash}     
    try:
        if metadata:
            with open(internal_metadata_json_file,"w") as f:
                json.dump(metadata, f)
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)
        channel = discord.utils.get(guild.text_channels, name="debug")
        await channel.send("admin pls help (savemeta):\n```\n{}\n```\n{}".format(exception_text, e))
            





    """try:
        needping = False
        for category in guild.categories:
            if "Bot Zone" in category.name:
                print("Sorting2",category.name)
                channel_names_unsorted = list(channel.name for channel in category.channels)
                channel_names = sorted(channel_names_unsorted)
            
                if not channel_names_unsorted == channel_names:
                    needping = True
                    channel = discord.utils.get(guild.text_channels, name="bootlog")
                    await channel.send('Sorting mid-battle {}, \nplease wait...'.format(category.name))
                    
                    print("Needs sorting",category.name)
                    for channel_name in channel_names:
                        print(channel_name)
                        await discord.utils.get(category.channels, name=channel_name).edit(position=channel_names.index(channel_name))
                        print(channel_name, channel_names.index(channel_name))
        if needping:
            channel = discord.utils.get(guild.text_channels, name="bootlog")
            await channel.send("Alright. Let's fight!")
    except Exception as e:
        exception_text = traceback.format_exc()
        exception_text = censor_exception(exception_text)
        print(exception_text)
        print(e)
        try:
            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (post-sort):\n```\n{}\n```\n{}".format(exception_text, e))
        except:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)"""
        
    

    

client.run(TOKEN)