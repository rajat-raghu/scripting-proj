import time
from datetime import datetime as dt

host_temp = "hosts"
host_path=r"c:\Windows\System32\drivers\etc\hosts"
redirect ="0.0.0.0"
website_list= ["account.jetbrains.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("working hours")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+ website+ "\n")
                    print(file.read())
            print(file.read())
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print(file.read())
        print("fun hours..")
    time.sleep(100)
