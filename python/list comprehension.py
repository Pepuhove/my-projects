#[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

nums=[2,5,9]
mylst=[value * 2 for value in nums]
mylst=map(lambda value:value*2,nums)
print(list(mylst))

tester = {'info':[{'name':'pepu', 'class':'advanced','age':29}, {'name':'yvonne','class':'wife','age':25}]}
import json
print(json.dumps(tester,indent=2))
inner_list=tester['info']
compri=[d['name']for d in inner_list]
print(list(compri))

def longlength(str):
   return [i for i in str if len (i)>=4]


print(longlength(['a','bcde','fghij']))

