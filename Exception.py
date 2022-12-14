import os,json,Main,Help
        
def netexception():
    jsonpath = f'{os.path.dirname(__file__)}\Config.json'
    cmd = input('无法连接服务器，请输入您的网络操作：').lower().title()
    if cmd == 'Exit': Main.user()
    elif cmd in ['Change','Restart']:
        if cmd == 'Change':
            myurl = input('服务器url：')
            with open(jsonpath,"w+") as url:
                json.dump({"Server":{"url":myurl}},indent = True,fp = url)
        Main.user()
    else:
        if cmd == 'Help': Help.nethelp()
        else: cmdexception()
        netexception()

def exception(ret:dict)->int:
    if ret.get('code') == 400:
        print(f'操作失败，请再次尝试，如果有疑问，请联系管理员或者NaCl')
        print(f'详情：{ret.get("body")}')
        return -1
    elif ret.get('code') == 405:
        print('请重新登陆')
        print(f'详情：{ret.get("body")}')
        Main.user()
        return 1
    else:
        print('操作成功')
        print(ret.get('code'))
        return 0

def cmdexception():
    print('输入了无效指令，请您重新输入，如果您忘记了指令，请输入Help')