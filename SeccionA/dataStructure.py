#!/usr/bin/python3
data ={'DataA':{'name':'One name','level':'One','Priority':'Highest',
       'Subdata':[{'name':'One nameSubDataA','level':'One','Priority':'Highest',
                   'Subdata':[]},
                  {'name':'One nameSubDataA2','level':'Two','Priority':'High', 
                   'Subdata':[{'name':'One nameSubDataAA','level':'One','Priority':'Highest', 
                                'Subdata':[]}]}
                 ]
               },
       'DataB':{'name':'One nameB','level':'Two','Priority':'Highest',
       'Subdata':[{'name':'One nameSubDataA','level':'One','Priority':'Highest',
                   'Subdata':[]}]}
      }

dC= {'DataC':{'name':'One nameC','level':'One','Priority':'High',
       'Subdata':[]}}

def recursiveShow(d,tabs):
    print('\t'*tabs,end='')
    print('name: '+d['name'])
    print('\t'*tabs,end='')
    print('level: '+d['level'])
    print('\t'*tabs,end='')
    print('Priority: '+d['Priority'])
    print()   
    for sD in d['Subdata']:
        recursiveShow(sD,tabs+1)


def show(data):
    for D, d in data.items():
        print(D)
        recursiveShow(d,1)
            
def addData(newData):
    for keyDic,value in newData.items():
        data[keyDic]=value

def main():
    print('Datos originales:')
    show(data)
    addData(dC)
    print('Datos nuevos agregados:')
    show(data)

if __name__ == '__main__':
    main()