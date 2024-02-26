class Agent:
    def __init__(self, codename, score):
        self.codename=codename
        self.score=score
agents = []
for _ in range(5):
    c,s =input().split()
    agents.append(Agent(c,int(s)))
agent_num = -1
m =10001
for idx in range(5):
    if m>agents[idx].score:
        m = agents[idx].score
        agent_num=idx


print(agents[agent_num].codename, agents[agent_num].score)