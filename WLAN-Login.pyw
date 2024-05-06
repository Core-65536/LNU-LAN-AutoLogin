import urllib,requests,urllib3
import subprocess,os
import time,json
import logging

def ReadConfig():
    global data
    #检测配置文件是否存在
    if not os.access("WLAN-cfg.json",os.R_OK):
        logging.error('Config file not found')
        exit()
    #读取配置文件
    cfg = open('WLAN-cfg.json','r')
    data = json.loads(cfg.read())
    cfg.close()

def isConnect():   
    try:
        urllib3.disable_warnings()
        req = requests.get('http://bing.com.cn',verify=False)
        if req.text.find('bing') != -1:
            return True
        else:
            return False
    except:
        return False

def SignIn():
    get = {}
    url = 'http://202.118.49.94:801/eportal/portal/login?callback=dr1003&login_method=1'
    url += '&user_account='+data['user_account']+'&user_password='+data['user_password']
    req = requests.get(url, data=get)
    if req.text.find('成功') != -1:
        logging.info('Sign in success')

def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s ----- %(message)s',
        level=logging.INFO,
        filename='WLAN-Net-Login.log',
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
            time.sleep(10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info('exit')
        exit()