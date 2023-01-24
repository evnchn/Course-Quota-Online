developer_max_worker_constant = 4 # 100 is obsolete. Will cause excessive CPU spikes

developer_use_new_differ = True # False is the old version. Rollback if all else fails! 
import newdiffer
from base64 import b64encode, b64decode

'''
def GetCeilIndex(arr, T, l, r, key):
 
    while (r - l > 1):
     
        m = l + (r - l)//2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
 
    return r
  
def LongestIncreasingSubsequence(arr, n):
 
    # Add boundary case,
    # when array n is zero
    # Depend on smart pointers
     
    # Initialized with 0
    tailIndices =[0 for i in range(n + 1)] 
 
    # Initialized with -1
    prevIndices =[-1 for i in range(n + 1)] 
     
    # it will always point
    # to empty location
    len_internal = 1
    for i in range(1, n):
     
        if (arr[i] < arr[tailIndices[0]]):
         
            # new smallest value
            tailIndices[0] = i
         
        elif (arr[i] > arr[tailIndices[len_internal-1]]):
         
            # arr[i] wants to extend
            # largest subsequence
            prevIndices[i] = tailIndices[len_internal-1]
            tailIndices[len_internal] = i
            len_internal += 1
         
        else:
         
            # arr[i] wants to be a
            # potential condidate of
            # future subsequence
            # It will replace ceil
            # value in tailIndices
            pos = GetCeilIndex(arr, tailIndices, -1,
                                   len_internal-1, arr[i])
  
            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i
         
    #print("LIS of given input")
    i = tailIndices[len_internal-1]
    constructarr = []
    while(i >= 0):
        constructarr.append(arr[i])
        #print(arr[i], " ", end ="")
        i = prevIndices[i]
    #print()
    
    constructarr.reverse()
    
    #print(constructarr)
  
    return constructarr # len_internal
    

def moveelem_discord(arr, elem, ind):
    if ind == len(arr):
        arr.remove(elem)
        arr.append(elem)
        return arr
    if ind == 1:
        arr.remove(elem)
        return [elem] + arr
    
    
    arr.remove(elem)
    arr.insert(ind-1, elem)
    return arr

def testing(arr, debug=False):
    moves = []
    # driver code
    #arr = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    arr_orig = list(arr)
    arr = list(arr)
    assert len(list(set(arr))) == len(arr)

    n = len(arr)
      
    LIS_output = LongestIncreasingSubsequence(arr, n)

    sorted_arr = list(sorted(arr))

    arr_with_flags = [(x, x in LIS_output) for x in arr]


    elem_not_in = list(elem for elem in arr if elem not in LIS_output)

    elem_not_in.sort()


    

    for elem in elem_not_in:
    
        arr_with_flags.remove(tuple((elem, False)))
        #print(arr_with_flags)
        if elem < min(x[0] for x in arr_with_flags if x[1]):
            arr_with_flags = [tuple((elem, 1))] + arr_with_flags
            moves.append((elem, 1))
            arr = moveelem_discord(arr, elem, 1)
            continue
            
        elif elem > max(x[0] for x in arr_with_flags if x[1]):
            arr_with_flags = arr_with_flags + [tuple((elem, 1))]
            moves.append((elem, len(arr)))
            arr = moveelem_discord(arr, elem, len(arr))
            continue
        else:
            ind = 0
            while True:
                if arr_with_flags[ind][1] and arr_with_flags[ind][0] > elem:
                    break
                ind += 1
                
            target_i = ind
                    
           
        new_index = target_i
        #print(new_index)
        if debug:
            print("move Elem[{}] to {}".format(elem, new_index))
        
        
        
        if target_i == -1:
            arr_with_flags.append(tuple((elem, 1)))
        else:
            arr_with_flags.insert(new_index, tuple((elem, 1)))
        
        
        moves.append((elem, target_i + 1))
        
        arr = moveelem_discord(arr, elem, target_i + 1)
            
    # arr = [x[0] for x in arr_with_flags]
    if not arr == sorted_arr:
        print(arr_orig)
        print(arr)
        print(arr_with_flags)
        print(sorted_arr)
        print("BAD!!!!!!!!!!!!!!!!!!!!!")
        return False
    return moves

###### HIGHLY EXPERIMENTAL CODE



'''
































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
from dotenv import load_dotenv

from discord.ext import tasks




import pathlib

latest_state_json_file = str(pathlib.Path(__file__).parent.absolute() / "latest_state.json")

internal_metadata_json_file = str(pathlib.Path(__file__).parent.absolute() / "internal_metadata.json")

my_location = str(pathlib.Path(__file__).absolute())

my_hash = sha256sum(my_location)

print(my_hash)

# input()



import asyncio
import concurrent.futures
import requests





'''
import ssl

FORCED_CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'
)
sslcontext = ssl.create_default_context()
# sslcontext.options |= ssl.OP_NO_SSLv3
# sslcontext.options |= ssl.OP_NO_SSLv2
# sslcontext.options |= ssl.OP_NO_TLSv1_1
sslcontext.options |= ssl.OP_NO_TLSv1_2
# sslcontext.options |= ssl.OP_NO_TLSv1_3
sslcontext.set_ciphers(FORCED_CIPHERS)'''

import aiohttp

import http3

client_requests = http3.AsyncClient()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot_identity = "kirito"
client = discord.Client(intents=discord.Intents.default())



async def do_request(method, url):
    '''response = await aiohttp.request(
        method, url, timeout=10
    )'''
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10, ssl=sslcontext) as response:
            return response








def censor_exception(exception_text):
    base_directory = os.path.expanduser("~")
    base_directory_split = base_directory.split("\\")
    base_directory_split[-1] = "Heathcliff"
    new_base_directory = "\\".join(base_directory_split)
    return exception_text.replace(__file__, "cardinal.py").replace(base_directory, new_base_directory)

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
        
    if ".SECT." in location:
        location = location.replace(".SECT.","-",1)
        
    if event == "add":
        return "\u001b[1;36m[ADD]\u001b[0;37m {}: \n{}".format(location, content)
    elif event == "remove":
        return "\u001b[1;35m[DEL]\u001b[0;37m {}: \n{}".format(location, content)
    elif event == "change":
        if str(content[0]).isdigit() and str(content[1]).isdigit():
            try:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{} -> {} ({})".format(location, content[0], content[1], "{}{}".format("+" if int(content[1]) > int(content[0]) else "", int(content[1]) - int(content[0])))
            except:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}\nto\n{}".format(location, content[0], content[1])
        elif set((str(content[0]), str(content[1]))) == set(("True", "False")):
            try:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{} -> {}".format(location, content[0], content[1])
            except:
                return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}\nto\n{}".format(location, content[0], content[1])
        return "\u001b[1;33m[CHG]\u001b[0;37m {}: \n{}\nto\n{}".format(location, content[0], content[1])
    else:
        return str(diff)
endpoint_ensured = "" 
def check_it_out(diff):
    global endpoint_ensured
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
    cc = location.split(".")[0]
    url = "{}subject/{}#{}".format(endpoint_ensured, cc[0:4], cc)
    
    fourdigits = endpoint_ensured.split("/")[-2]
    
    # http://evn.asuscomm.com:2280/2230COMP1021
    
    url2 = "http://evn.asuscomm.com:2280/{}{}".format(fourdigits, cc)
    
    return "{}\n{}".format(url2, url)
    
def is_important(diff):
    event, location, content = diff
    if isinstance(location, list):
        location = ".".join(str(x) for x in location)
    unimportant = ("Wait", )
    for unimportant_strings in unimportant:
        if unimportant_strings in location:
            return False
    return True



channels_to_remove = [str(i).rjust(4, "0") for i in range(60)]
channels_to_remove += [(i+"-important") for i in channels_to_remove]
channels_to_remove = '''acct,aesf,aiaa,amat,bibu,bien,bsbe,btec,cbme,ceng,chem,chms,ciem,civl,cmaa,comp,core,cpeg,csit,dasc,dbap,dsaa,dsct,econ,eemt,eesm,elec,emba,emia,eneg,engg,entr,envr,envs,eoas,evng,evsm,fina,ftec,gbus,gfin,gned,hlth,hmma,huma,ibtm,ieda,iimp,imba,intr,iota,ipen,isdn,isom,jeve,labu,lang,lifs,maed,mafs,mark,mass,math,mech,mesf,mfit,mgcs,mgmt,mics,mile,mimt,msbd,msdm,mtle,nano,oces,pdev,phys,ppol,rmbi,roas,sbmt,scie,seen,shss,smmg,sosc,sust,temg,ugod,urop,wbba,acct-important,aesf-important,aiaa-important,amat-important,bibu-important,bien-important,bsbe-important,btec-important,cbme-important,ceng-important,chem-important,chms-important,ciem-important,civl-important,cmaa-important,comp-important,core-important,cpeg-important,csit-important,dasc-important,dbap-important,dsaa-important,dsct-important,econ-important,eemt-important,eesm-important,elec-important,emba-important,emia-important,eneg-important,engg-important,entr-important,envr-important,envs-important,eoas-important,evng-important,evsm-important,fina-important,ftec-important,gbus-important,gfin-important,gned-important,hlth-important,hmma-important,huma-important,ibtm-important,ieda-important,iimp-important,imba-important,intr-important,iota-important,ipen-important,isdn-important,isom-important,jeve-important,labu-important,lang-important,lifs-important,maed-important,mafs-important,mark-important,mass-important,math-important,mech-important,mesf-important,mfit-important,mgcs-important,mgmt-important,mics-important,mile-important,mimt-important,msbd-important,msdm-important,mtle-important,nano-important,oces-important,pdev-important,phys-important,ppol-important,rmbi-important,roas-important,sbmt-important,scie-important,seen-important,shss-important,smmg-important,sosc-important,sust-important,temg-important,ugod-important,urop-important,wbba-important,misc,misc-important,debug,bootlog,able'''.split(",")

channels_to_remove = []

@client.event
async def on_ready():
    global channels_to_remove
    for guild in client.guilds:
        if guild.name == GUILD:
            break
            
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
    
    for important_preboot_channels in ("debug", "bootlog", "updates"):
        channel = discord.utils.get(guild.text_channels, name=important_preboot_channels)
        if not channel:
            try:
                channel = await guild.create_text_channel(important_preboot_channels, category=category)
                await channel.edit(type=discord.ChannelType.news)
                print(channel.type)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                await guild.create_text_channel(important_preboot_channels)
                
                
                
    
    for channel_name in channels_to_remove:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if channel:
            print("Removing channel",channel_name)
            await channel.delete()
    channels_to_remove = []
    try:
        debug_write_to_file = False

        endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/'

        endpoint = requests.head(endpoint, allow_redirects=True).url

        print(endpoint)
        if fake_endpoint:
            endpoint = 'https://w5.ab.ust.hk/wcq/cgi-bin/2210/'
        url = endpoint

        page = requests.get(url)

        soup = bs.BeautifulSoup(page.text,'lxml')

        depts = soup.select('.depts')[0]
        
        depts_plus = [(dept.get_text(""),("PG" if dept.has_attr('class') and "pg" in dept['class'] else "UG")) for dept in depts]
        depts_plus_dict = dict(depts_plus)
        depts = depts.get_text("\n").split("\n")
        
        expected_channel_names = depts
        expected_channel_names_internal = list(depts)
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
    
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    
    await channel.send('Waking up. ')
    
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
    for category in guild.categories:
        
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
                    print(channel_name, channel_names.index(channel_name))
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    await channel.send("Alright. Let's fight!")
    
    for category in guild.categories:
        if "Bot Zone" in category.name:
            count = 0
            for channel in category.channels:
                if channel.type != discord.ChannelType.news:
                    count += 1
            if count:
                channel = discord.utils.get(guild.text_channels, name="bootlog")
                await channel.send('Converting {} channel{} to announcements\nin {}, please wait...'.format(count, "" if count == 1 else "s", category.name))
                for channel in category.channels:
                    if channel.type != discord.ChannelType.news:
                        await channel.edit(type=discord.ChannelType.news)
    channel = discord.utils.get(guild.text_channels, name="bootlog")
    await channel.send("Alright. Let's fight!")
    
    
    myLoop.start()

# last_valid_endpoint is endpoint_ensured
last_valid_page = None
@tasks.loop(seconds = 90) # repeat after every 10 seconds
async def myLoop():
    global last_valid_page
    global endpoint_ensured
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
            if last_valid_page:
                # use newer endpoint determination and course list determination. 
                # iterate through course list until get a fresh page
                # then go on
                print("---REVO - FLASHBACK---")
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    loop = asyncio.get_event_loop()
                    futures = [

                        loop.run_in_executor(
                            executor, 
                            bs.BeautifulSoup, 
                            ptxt, 
                            'lxml'
                        )
                        for ptxt in [last_valid_page.text]
                    ]
                    rs2_beautifulsoup = await asyncio.gather(*futures)
                soup = rs2_beautifulsoup[0]
                endpoint = soup.select(".termselect > a")[0]['href']
                endpoint = urljoin(last_valid_page.url, endpoint)
                endpoint_ensured = endpoint
                print(endpoint)
                
                depts = soup.select('.depts')[0]
                depts = depts.get_text("\n").split("\n")
                
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
            #os.system("cls")

            
            
            
            
            
            urls = ['{}subject/{}'.format(endpoint, dept) for dept in depts]
            
            
            
            
            #rs = (grequests.get(u, timeout=10) for u in urls)
            #rs2 = grequests.map(rs)
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
            '''loop.run_in_executor(
                executor, 
                requests.get, 
                url
            )'''
            print(depts)
            
            
            for page in rs2:
                if page.status_code == 200:
                    last_valid_page = page
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
            for i, dept in enumerate(tqdm(depts)):
                

                '''url = '{}subject/{}'.format(endpoint, dept)
                print(url)
                #url = "http://localhost:8000/{}".format(dept)

                page = await client_requests.get(url, timeout=10)
                #page = await do_request("GET",url)
                
                assert page.status_code == 200'''
                
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
                soup = rs2_beautifulsoup[0]
                #soup = bs.BeautifulSoup(page.text,'lxml')

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
                    keys = [k.text.replace(" & ", "_N_") for k in keys]
                    for row in coursetable.select('tr')[1:]:
                        fields = row.select("td")
                        
                        if buffered_coursetable_row and len(fields) == 3: # is an extension
                            '''buffered_coursetable_row_2 = [None for i in range(len(buffered_coursetable_row))]
                            buffered_coursetable_row_2 = ["" for i in range(len(buffered_coursetable_row))]
                            buffered_coursetable_row_2[1] = "; {}".format(fields[0].get_text(separator="_"))
                            buffered_coursetable_row_2[2] = "; {}".format(fields[1].get_text(separator="_"))
                            buffered_coursetable_row_2[3] = "; {}".format(fields[2].get_text(separator="_"))'''
                            #print(buffered_coursetable_row, buffered_coursetable_row_2)
                            '''buffered_coursetable_row = [i if not isinstance(i, str) else str(i)+str(k) for i,k in zip(buffered_coursetable_row, buffered_coursetable_row_2)]'''
                            buffered_coursetable_row[1].append(fields[0].get_text(separator="_"))
                            buffered_coursetable_row[2].append(fields[1].get_text(separator="_"))
                            buffered_coursetable_row[3].append(list(fields[2].stripped_strings))
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
                                    quotadetail_info = list(field.select(".quotadetail")[0].stripped_strings)[1:]
                                elif i in (3, ):
                                    buffered_coursetable_row[i] = [list(field.stripped_strings)]
                                elif i in (1,2):
                                    buffered_coursetable_row[i] = [field.get_text(separator="_")]
                                elif i in (4,5,6):
                                    buffered_coursetable_row[i] = int(field.get_text(separator="_"))
                                elif i in (8,):
                                    mkdict = {}
                                    if field.select(".popup.consent"):
                                        mkdict["consent"] = True
                                    else:
                                        mkdict["consent"] = False
                                    if field.select(".popup.classnotes"):
                                        # mkdict["info"] = ''.join(field.select(".popup.classnotes")[0].get_text(separator="; ").splitlines()) # no need newlines here. 
                                        mkdict["info"] = list(field.select(".popup.classnotes")[0].stripped_strings)
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
                    
                    
                    sections_keyfield = list(coursetable_list_dicts[0].keys())[0]
                    
                    
                    
                    coursetable_list_dicts_2 = {x.pop(sections_keyfield).replace(" ",""):x for x in coursetable_list_dicts}
                    
                    if course_table_length_mismatch == True:
                        allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECT":coursetable_list_dicts_2, "_SECTIONS_keyfield": sections_keyfield, "FAILURE":"course_table_length_mismatch", "TABLE_COUNT":coursetable_len}
                    else:
                        allcourses_dict[coursecode] = {"COURSE_INFO":courseinfo_dict, "COURSE_FLAGS": course_flags, "SECT":coursetable_list_dicts_2, "_SECTIONS_keyfield": sections_keyfield}
                    
                    
                    
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
            
            with open(latest_state_json_file,"r") as f:
                allcourses_dict_old = json.load(f)

            #pyperclip.copy(output)
            
            if allcourses_dict_old and allcourses_dict:
                if developer_use_new_differ:
                    the_diffs = newdiffer.diff2(allcourses_dict_old, allcourses_dict)
                else:
                    the_diffs = list(dictdiffer.diff(allcourses_dict_old, allcourses_dict))
                for diff in the_diffs: 
                    if len(diff[1])==8 and diff[1][4:8].isdigit(): ## just a course 
                        diff = list(diff)
                        diff[2] = "<AN ENTIRE COURSE>"
                    if not diff[1]:
                        '''with open("logfile.txt", "a") as lf:
                            lf.writelines(["###MISC-IMPORTANT###", str(diff), datetime.now().strftime("%H:%M:%S"), "------"])
                            channel = discord.utils.get(guild.text_channels, name="debug")
                            await channel.send("check logfile.txt to debug strange misc-important NOW!")'''
                        # Adding / deleting from root element, fake things a little. 
                        behaviour = diff[0]
                        for course in diff[2]:
                            #os.system("cls")
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
                        if diff[1] and (expected_channel_name in diff[1] or expected_channel_name in diff[1][0]):
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
                json_hash = sha256sum(latest_state_json_file)
                print(json_hash)
                channel = discord.utils.get(guild.text_channels, name="hashes-{}".format(bot_identity))
                messages = [message async for message in channel.history(limit=1)]
                if not messages:
                    await channel.send(json_hash)
                else:
                    await messages[0].edit(content=json_hash)
                #await channel.send(json_hash)
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (savedict):\n```\n{}\n```\n{}".format(exception_text, e))
            
        metadata = {"HKUST Server Endpoint": endpoint_ensured, "CQO (SHA256-Base64)": my_hash}
        try:
            with open(internal_metadata_json_file, "r") as f:
                metadata_old = json.load(f)
            
            
            if metadata and metadata_old:
                for diff in list(dictdiffer.diff(metadata_old, metadata)):
                    ignore_updates = True
                    _, area, change = diff
                    channel = discord.utils.get(guild.text_channels, name="updates")
                    await channel.send("```\nUpdated {} from:\n{}\nto\n{}\n```{}\n_ _".format(area, change[0], change[1], "As such, {} notification{} {} safely ignored. ".format(len(notif), "" if len(notif) == 1 else "s", "is" if len(notif) == 1 else "are") if notif else "Doesn't matter, no notifications anyways. "))
                    del notif
                    notif = {}
            else:
                raise Exception("Either metadata is nullish. ")
        
        except Exception as e:
            exception_text = traceback.format_exc()
            exception_text = censor_exception(exception_text)
            print(exception_text)
            print(e)

            channel = discord.utils.get(guild.text_channels, name="debug")
            await channel.send("admin pls help (showmeta):\n```\n{}\n```\n{}".format(exception_text, e))
        
        #time.sleep(300)
        try:
            todos = []
            

            
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
                        if importancy == is_important(sub_v) and filter_phantom_change(sub_v):
                            sending_string = "```ansi\n{}\n```See: {}\n_ _".format(preetify_diff(sub_v),check_it_out(sub_v))
                            ## Added ANSI formatting here
                            print(sending_string)
                            if len(sending_string) < 1900:
                                todos.append(channel.send(sending_string))
                            else:
                                with open("logfile.txt", "a") as lf:
                                    lf.writelines(["###TOO-LONG-STRING###", sending_string, datetime.now().strftime("%H:%M:%S"), "------"])
                                    channel = discord.utils.get(guild.text_channels, name="debug")
                                    await channel.send("check logfile.txt to debug exceed 2000 characters NOW!")
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
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="{}'s data".format(datetime.now().strftime("%H:%M:%S"))))
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
            
            
            
    try:
        needping = False
        for category in guild.categories:
            if "Bot Zone" in category.name:
                print("Sorting",category.name)
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
            print(e)
        
    

    

client.run(TOKEN)