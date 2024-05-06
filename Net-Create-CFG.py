import os,json

def CreateConfig():
    print('Creating config file...')
    #创建配置文件
    data = {}
    data['DDDDD'] = input('Account:')
    data['upass'] = input('Password:')
    data['0MKKey'] = ''
    #写入配置文件
    cfg = json.dumps(data)  #将字典转换为字符串
    file = open('cfg.json','w')
    file.write(cfg)
    file.close()

def CreateWLANConfig():
    print('Creating config file...')
    #创建配置文件
    data = {}
    data['user_account'] = input('Account:')
    data['user_password'] = input('Password:')
    #写入配置文件
    cfg = json.dumps(data)  #将字典转换为字符串
    file = open('WLAN-cfg.json','w')
    file.write(cfg)
    file.close()

def main():
    mode = input('LAN-Config OR WLAN-Config (1/2)?\n')
    if  mode == 1:
        if os.path.exists('cfg.json'):
            flag = input('Config file already exists, overwrite? (y/n)\n')
            if flag == 'n' or flag == 'N':
                return
            else:
                CreateConfig()
        else:
            CreateConfig()
    else:
        if os.path.exists('WLAN-cfg.json'):
            flag = input('Config file already exists, overwrite? (y/n)\n')
            if flag == 'n' or flag == 'N':
                return
            else:
                CreateWLANConfig()
        else:
            CreateWLANConfig()
    

if __name__ == '__main__':
    main()