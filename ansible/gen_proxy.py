LIST_SERVER = [
    "18.142.139.250:8888",
    "13.212.107.241:8888",
    "13.214.196.242:8888",
    "13.214.220.55:8888",
    "13.251.38.8:8888",
    "13.214.159.223:8888",
    "13.214.200.170:8888",
    "18.141.166.77:8888",
    "13.229.143.136:8888",
    "13.212.166.158:8888",
    "54.179.91.224:8888",
    "54.169.59.221:8888",
    "13.215.45.129:8888",
    "52.77.245.113:8888",
    "18.139.209.225:8888",
    "13.250.47.219:8888",
    "54.169.74.227:8888",
    "13.215.205.47:8888",
    "54.151.145.240:8888",
    "13.250.102.139:8888",
    "54.254.164.69:8888",
    "18.142.254.217:8888",
    "18.139.115.27:8888",
    "52.221.183.155:8888",
    "18.142.182.217:8888",
    "13.215.184.223:8888",
    "52.221.207.222:8888",
    "18.139.108.203:8888",
    "18.141.188.232:8888",
    "54.169.160.160:8888",
    "18.141.142.227:8888",
    "13.213.42.213:8888",
    "3.1.83.232:8888",
    "18.139.225.109:8888",
    "54.169.55.179:8888",
    "18.139.208.219:8888",
    "18.141.138.117:8888",
    "52.221.188.112:8888",
    "13.229.113.109:8888",
    "18.142.177.227:8888",
    "13.212.247.19:8888",
    "18.143.75.65:8888",
    "18.136.210.144:8888",
    "18.136.208.91:8888",
    "13.213.51.160:8888",
]



ALL_STRING = ""
PRE = "ssh -i ~/seta/manhtd6932/crawl-data.pem -n -f ubuntu@"
POST = " > /dev/null 2>&1 &"
index = 3_000_000
for ind, link in enumerate(LIST_SERVER):
    # if ind % 2 ==0:
    #     COMAND = f"cd /home/ubuntu/bonbanh_dist/ && python3 yahoo.py --start {index + 40_000} --end {index + 60_000} --thread 1"
    # else:
    #     COMAND = f"cd /home/ubuntu/bonbanh_dist/ && python3 yahoo.py --start {index + 60_000} --end {index + 80_000} --thread 1"
    #     index += 100_000
    ALL_STRING += PRE+ link.split(":")[0] + " '/home/ubuntu/.local/bin/proxy --hostname 0.0.0.0 --port 8888 --enable-web-server --plugins proxy.plugin.RedirectToCustomServerPlugin > /dev/null 2>&1 &'\n"
    

with open("proxy2.sh", "w+") as f:
    f.write(ALL_STRING)