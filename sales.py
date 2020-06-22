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
        print("Query for "+i[0])
        if i[1]=='1':
            for ag in Agents:
                if ag.is_available and ag.checkroles(i[0].split(",")):
                    print("Assigning Query to Agent "+ag.name)
        if i[1]=='2':
            max_agent = max(Agents,key=attrgetter('available_since'))
            print("Assigning Query to Agent "+max_agent.name)
        if i[1]=='3':
            random_agent=choice(Agents)
            print("Assigning Query to Agent "+random_agent.name)

if __name__=='__main__':
    Agents=[]
    queue=[]
    n=int(input())
    q=int(input())
    for i in range(n):
        Agents.append(Agent(input().split()))
    for i in range(q):
        queue.append(input().split())
    agent_assign(queue,Agents)