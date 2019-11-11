import linecache,time
# new_str = re.sub('[^\w\u4e00-\u9fff]+', '','江苏 » 无锡市:婚礼司仪roger')
# print(new_str)
# with open(r'C:\Users\Administrator\Desktop\\The.Professor.srt', 'rb') as f:
    # encoding='gb18030'
    # new_str = re.sub('[^\w\u4e00-\u9fff]+', '',f)
    # print(f.read())
    # str_wait = f.read()
    # # print("*"*30,str_wait)
    # # print(type(str_wait))

    # new_str = re.sub('[^\w\u4e00-\u9fff]+', '',str(str_wait, encoding = "utf-8"))
    # print("*"*30,new_str)   

# new_str = linecache.getline(r'C:\Users\Administrator\Desktop\\The.Professor.srt',4)
global n
n = 0
global i
i = 0
global shuzu
shuzu = [3,4,8,9]

with open(r'C:\Users\Administrator\Desktop\\The.Professor.srt','rb') as f:
    txt = str(f.read(),encoding = "utf-8")
    # data = txt.read().decode('utf-8')      #python3一定要加上这句不然会编码报错！

    #获取txt的总行数！
    n = int(txt.count('\n')/10)
    print("总行数",n)
    # print(new_str)


while(1):
 with open(r'C:\Users\Administrator\Desktop\\The.Professor1.srt', 'a+') as f:
    for x in range(0,4):
        print(shuzu[x])
        new_str = linecache.getline(r'C:\Users\Administrator\Desktop\\The.Professor.srt',shuzu[x])
        # print(new_str)
        f.write(new_str+' --- ')
        # time.sleep(0.5)
        shuzu[x]+=10
        # print(shuzu[x])
        print('new:'+str(x)+'/'+str(i)+'/'+str(n))
    i+=1 
    if(n==i):
        quit()

