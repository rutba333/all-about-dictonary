student_data={'d1':
{'name':['Sara'],
'class':['v'],
'subject_intergation':['english,math,science']},


'd2':
{'name':['David'],
'class':['v'],
'subject_intergation':['english,math,science']},

'd3':
{'name':['Sara'],
'class':['v'],
'subject_intergation':['english,math,science']},

'd4':
{'name':['Surya'],
'class':['v'],
'subject_intergation':['english,math,science']},
}

result={}

for key,value in student_data.items():
  if value not in result.values():
        result[key]=value

print(result)
