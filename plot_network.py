# libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# read the 'nodes.txt' file
nodes = pd.read_csv('nodes.txt', sep=" ", header=None)

# create empty lists
node_id = []
node_state = []
node_group = []

# appending the elements of first column of nodes variable to node_id
# appending the elements of second column of nodes variable to node_state
for i in range(0,len(nodes[0])):
    node_id.append(nodes[0][i])
    node_state.append(nodes[1][i])

# appending the specific name of group fe. 'group1' to node of state 'S'
# this is used to specific colors for diffrent types of nodes : S, I R
for state in node_state:
    if state == 'S':
        node_group.append('group1')
    if state == 'I':
        node_group.append('group2')
    if state == 'R':
        node_group.append('group3')
   
# read the 'edges.txt' file  
edges = pd.read_csv('edges.txt', sep=" ", header=None)

# create empty lists of pair dependencies (X - A node, Y - B node)
X = []
Y = []

# appending the elements of first column of edges variable to X
# appending the elements of second column of edges variable to Y
for i in range(0,len(edges[0])):
    X.append(edges[0][i])
    Y.append(edges[1][i])

# creating a dictionary, for label the nodes and specific color:
# {0: 'S', 1: 'R', 2: 'S', 3: 'S', 4: 'I', 5: 'S', 6: 'I', 7: 'S', 8: 'R', 9: 'S'}
labeldict = dict(zip(node_id,node_state))

# build a dataframe from our connections
df = pd.DataFrame({ 'from':X, 'to':Y})

# and a data frame with characteristics for nodes
carac = pd.DataFrame({ 'ID':['S', 'I', 'R'], 'myvalue':['group1','group2', 'group3']})

# building graph
G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph() )
 
G.nodes()

# need to reorder carac to assign the good color to each node
carac= carac.set_index('ID')
carac=carac.reindex(G.nodes())
 
# need to transform categorical column in a numerical value: group1->1, group2->2...
carac['myvalue']=pd.Categorical(carac['myvalue'])
carac['myvalue'].cat.codes

fig = plt.figure(figsize=(50,50))

# custom the nodes:
nx.draw(G, labels=labeldict, node_color=carac['myvalue'].cat.codes, width=1, edge_color='#696969', with_labels = False, cmap=plt.cm.Set1, node_size=100,font_size=10)

# Setting it to how it was looking before.                                                                                                              

fig.set_facecolor('w')
plt.show()

#save the graph as pdf
fig.savefig("plot5.pdf")