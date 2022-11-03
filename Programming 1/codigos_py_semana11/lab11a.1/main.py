"""
dict={1:'Geeks',
      2:'For',
      3:{'A':'Welcome','B':'To','C':'Geeks'}}
print(dict)


dict={'Dict1':{},'Dict2':{}}
print(dict)

dict={'Alumno1':{'name':'Ali','age':'19'},
      'Alumno2':{'name':'Bob','age':'25'}}
print(dict)
print(dict["Alumno1"])

dict={'Dict1':{1:'G',2:'F',3:'G'},
      'Dict2':{'Name':'Geeks',1:[1,2]}}
print(dict)


people={1:{'nombre':'Juan','edad':'27','sexo':'M'},
        2:{'nombre':'Maria','edad':'22','sexo':'F'}}
print(people[2]['nombre'])
print(people[2]['edad'])
print(people[2]['sexo'])

people={1:{'name':'John','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'}}

people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='No'
print(people)

people={1:{'name':'John','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'},
        3:{'name':'Luna','age':'24','sex':'Female','married':'No'}}

people[4]={'name':'Peter','age':'29','sex':'Male','married':'Yes'}
print(people)

people={1:{'name':'John','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'},
        3:{'name':'Luna','age':'24','sex':'Female'},
        4:{'name':'Peter','age':'29','sex':'Male'}}
del people[3], people[4]
print(people)

people={1:{'name':'John','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'},
        3:{'name':'Luna','age':'24','sex':'Female','married':'No'},
        4:{'name':'Peter','age':'29','sex':'Male','married':'Yes'}}
del people[3]['married']
del people[4]['married']
print(people)
"""
people={1:{'name':'John','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'},
        3:{'name':'Luna','age':'24','sex':'Female','married':'No'},
        4:{'name':'Peter','age':'29','sex':'Male','married':'Yes'}}
for p_id,p_info in people.items():
    print("\nPersonID:",p_id)
    for key in p_info:
        print(key+':',p_info[key])
