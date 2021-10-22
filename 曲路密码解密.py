
def decryption(crypto,h1,h2):
    huoqu = crypto
    a = 0
    m = []
    c = ''
    for x in range(len(huoqu)):
        c += huoqu[x]
        a += 1
        if(a == h1):
            m.append(c)
            c = ''
            a = 0
        else:
            pass
    a = 0
    chongpai = []
    for x in range(len(m)):
        a += 1
        en = []
        if(a % 2 != 0):
            paikai = m[x]
            huan = paikai[0]
            huan2 = paikai[len(paikai) - 1]
            for x in range(len(paikai)):
                en.append(paikai[x])
            en[0] = huan2
            en[len(en) -1 ] = huan
            fuck = ''
            for j in range(len(en)):
                fuck += en[j]
            chongpai.append(fuck)
        else:
            chongpai.append(m[x])
    zaipai = []
    changdu = len(chongpai)
    print(chongpai)
    for j in range(len(chongpai)):
        changdu -=1
        zaipai.append(chongpai[changdu])

    flag = ''
    print(zaipai)
    for j in range(h1):
        for t in range(h2):
            flag += zaipai[t][j]
    return flag
if __name__ == '__main__':
    miwen = input('''
    曲路密码解密^^
    请输入密文：
    ''')
    hang = input('    行数:')
    lie = input('    列数:')
    #miwen = '}ey{r@gaga_1pulf0_'
    print('\n')
    print('--------------------------------------------------->')
    print('''
    [*] 解密成功：%s
    '''%(decryption(miwen,int(hang),int(lie))))