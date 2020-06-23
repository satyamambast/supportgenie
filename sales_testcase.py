import collections
from operator import attrgetter
from random import choice
class Agent:
    def __init__(self,attrlist):
        self.name=attrlist[0]
        if attrlist[1]=="True":
            self.is_available=True
        else:
            self.is_available=False
        self.available_since=int(attrlist[2])
        self.roles=attrlist[3].split(",")
    def checkroles(self,role):
        if collections.Counter(self.roles)==collections.Counter(role):
            return True
        return False

def agent_assign(queue,Agents):
    for i in queue:
        suitable_agents=[x for x in filter(lambda a: a.checkroles(i[0].split(",")),Agents)]
        if len(suitable_agents)==0:
            print("All suitable agents are busy right now for query"+i[0])
            continue
        print("Query for "+i[0],end=" ")
        if i[1]=='1':
            print(": Using Method 1(All Available Agents)")
            for ag in suitable_agents:
                print("Assigning Query to Agent "+ag.name)
        if i[1]=='2':
            print(": Using Method 2(Least Busy)")
            max_agent = max(suitable_agents,key=attrgetter('available_since'))
            print("Assigning Query to Agent "+max_agent.name)
        if i[1]=='3':
            print(": Using Method 3(Random Assign)")
            random_agent=choice(suitable_agents)
            print("Assigning Query to Agent "+random_agent.name)
if __name__=="__main__":
    with open("testcase.txt","r") as file:
        testcase=file.readlines()
    Agents=[]
    queue=[]
    n=int(testcase[0].strip())
    q=int(testcase[1].strip())
    pointer=2
    for i in range(n):
        agnt=testcase[pointer].split()
        if agnt[1]=='True':
            Agents.append(Agent(agnt))
        pointer+=1
    for i in range(q):
        queue.append(testcase[pointer].split())
        pointer+=1
    #print(queue)
    if len(Agents)!=0:
        agent_assign(queue,Agents)
    else:
        print("All Agents are busy")