## How the plot_network.py script works?

* The plot_network script was written in Python language. It draws the neural netowrk diagrams from a text data file.
* The script uses three libraries (pandas, networkxx and matplotlib.pyplot).
* First the script reads the file ‘nodes.txt’, where is the number of nodes and its specific state written. 
Then it creates empty lists, where we can store the node id, node state, and the nodes of specific color. 
After that in a for loop we add the first column from file nodes.txt to node_id and second column form file nodes.txt to node_state list. 
After that we append the node_id of diffrent node_state to the blue, red and green_nodes
At second step we read the data about edges to edges variable from the text file ‘edges.txt’.
After that we generate new G graph using networkx.Graph() method.
Then we add edges to the graph using G.add_edges() method. As firt argument of the method we give the edges.txt first column as edges[0][i]. As second argument of the method we give the edges.txt second column as edges[1][i].
Then we create a dictionary, for labeling the nodes. 
We create new fig variable with plt.figure(figsize(x,y)) value. After that we draw the nodes, edges and the legend of our network.
At the end we show the plot and save it with big dpi in PDF and PNG file format.
