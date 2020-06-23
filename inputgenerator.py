import random
import string

n=int(input("Enter the number of Agents "))
q=int(input("Enter the number of Queries "))
salestags=["Spanish","English","Tech","Sales","Python"]
test_case=str(n)+"\n"+str(q)
tags=[]
for i in range(n):
    agent_case=''.join(random.choice(string.ascii_uppercase) for i in range(4))
    agent_case+=" "+random.choice(["True","True","False"])+" "
    agent_case+=str(random.randint(1,40))+" "
    n_tags=random.randint(1,3)
    agent_tags=random.choice(salestags)+","
    for i in range(n_tags-1):
        tag=""
        while True:
            tag=random.choice(salestags)
            if tag not in agent_tags:
                agent_tags+=tag+","
                break
    agent_case+=agent_tags[:-1]
    tags.append(agent_tags[:-1])
    test_case+="\n"+agent_case
for i in range(q):
    query=random.choice(tags)+" "+str(random.randint(1,3))
    test_case+="\n"+query

print(test_case)
with open("testcase.txt",'w') as testcasefile:
    testcasefile.write(test_case)