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

def main():
    if os.path.exists('cfg.json'):
        flag = input('Config file already exists, overwrite? (y/n)\n')
        if flag == 'n' or flag == 'N':
            return
        else:
            CreateConfig()
    else:
        CreateConfig()

if __name__ == '__main__':
    main()