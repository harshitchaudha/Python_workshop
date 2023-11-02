employees= ['Corey', 'Jim', 'Steve', 'April', 'Judy', 'Jean', 'John', 'Jane']
gym_member= ['April', 'John', 'Corey']
developers=['Jody', 'Corey', 'Steven', 'Jane', 'April']

gym=set(gym_member)
dev=set(developers)
intersection=gym.intersection(dev)
print(intersection)