import json
import xlrd
import random



def import_xl(path):
    data=xlrd.open_workbook(path)
    table=data.sheets()[0]
    data_list=[]
    data_list.extend(table.col_values(0))
    return data_list
def writeJson(path,content):
    with open(path, 'w') as f:
        json.dump(content, f)
def readJson(path):
    with open(path, 'r') as f:
        content= json.load(f)
    return content
def dic_to_list(dicname):
    listname = []
    num = len(dicname)
    for i in range(0, num):

        name = (dicname.get(str(i)))
        listname.append(name)
    return listname

def parter(name):
    #way1找到所有组合的方式
    # name_two=copy.deepcopy(name)
    # for i in name:
    #     name_two.remove(i)
    #     for j in name_two:
    #        if i is not j:
    #            group=[i,j]
    #            grouppool.append(group)
    #
    # print(grouppool)
    grouppool = []
    for i in range(0,len(name)):
        for j in range(i+1,len(name)):
            grouppool.append([name[i],name[j]])
    return(grouppool)
def daluan(x,len):
    a = random.sample(x, len)
    return a

def selet_group(grouppool,desknumber):
    k = 0
    sg = [[]]

    for group in grouppool:
        if k <= desknumber*2:
            a=yanzheng(group,sg)
            if a==1:
               sg.append(group)
               k=k+1
    sg.remove([])



    return sg

def yanzheng(group,sg):
    a=1
    for j in sg:
        if group[0] in j or group[1] in j:
            a=0
    return a

def main(a):
    total = []
    name = daluan(a,len(a))
    grouppool=parter(name)
    desknumber=int(len(name)/4)
    count = 0
    while len(grouppool)>0:
        sg=selet_group(grouppool,desknumber)
        total.append(sg)
        for i in sg:
            grouppool.remove(i)
        count=count+1
    return total
    # print("count=",count)
if __name__ == '__main__':
    path = "C:/Users/Admin/PycharmProjects/guandan/guandan2/data.xls"
    a = import_xl(path)
    total=main(a)
    print(total)
