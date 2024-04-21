import urllib,requests,urllib3
import subprocess,os
import time,json
import logging

def ReadConfig():
    global data
    #检测配置文件是否存在
    if not os.access("cfg.json",os.R_OK):
        logging.error('Config file not found')
        exit()
    #读取配置文件
    cfg = open('cfg.json','r')
    data = json.loads(cfg.read())
    cfg.close()

def isConnect():   
    try:
        urllib3.disable_warnings()
        req = requests.get('http://www.bing.com.cn',verify=False)
        if req.status_code == 200:
            return True
    except:
        return False

def SignIn():
    url = 'http://202.118.62.242/login?'
    req = requests.post(url, data=data)
    if req.status_code == 200:
        logging.info('Sign in success')

def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s ----- %(message)s',
        level=logging.INFO,
        filename='Net-Login.log',
        filemode='a',
    )
    ReadConfig()
    logging.info('Checking...')
    while True:
        if os.access("Shutdown.txt",os.R_OK):
            logging.info('Shutdown signal received')
            os.remove("Shutdown.txt")
            exit()
        flag = isConnect()
        if not flag:
            logging.info('Not connected, signing in...')
            SignIn()
        else:
            time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info('exit')
        exit()