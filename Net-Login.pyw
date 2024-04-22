#Copyright 2024.4.22 By Core_65536
#Version : 1.0.0

import urllib,requests,urllib3
import subprocess,os
import time,json
import logging,socket
import sys

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

#检测网络连接
def isConnect():
    url = 'http://cn.bing.com/'
    try:
        urllib3.disable_warnings()
        #检测是否能访问bing & 获取重定向后的url
        req = requests.get(url,verify=False)
        logging.info('Got url = '+req.url)
        #如果重定向到bing则说明已经登录
        if req.url.find('bing') != -1:
            return True
        else:
            return False
    except:
        return False
    
def SignIn():
    url = 'http://cn.bing.com/'
    #在未登录情况下,重定向获取登陆界面url
    try:
        urllib3.disable_warnings()
        req = requests.get(url,verify=False)
        url = req.url
    except:
        return
    #拼接登陆url
    url = url+'/login?'
    logging.info('Login Server: '+url)
    #构造登陆数据并发送
    req = requests.post(url, data=data)
    #判断是否成功登陆
    if req.status_code == 200:
        logging.info('Sign in success')
    else:
        logging.error('Sign in failed'+str(req.status_code))

def main():
    #判断日志文件是否过大
    if os.stat('Net-Login.log').st_size > 1000 :
        os.remove('Net-Login.log')
    #初始化日志
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s ----- %(message)s',
        level=logging.INFO,
        filename='Net-Login.log',
        filemode='a',
    )
    ReadConfig()
    logging.info('Checking...')
    while True:
        #接受程序终止信号
        if os.access("Shutdown.txt",os.R_OK):
            logging.info('Shutdown signal received')
            os.remove("Shutdown.txt")
            exit()
        flag = isConnect()
        #如果未连接则尝试登陆
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