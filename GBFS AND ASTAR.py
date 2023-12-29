#use colab for excecution
import networkx as nx
import queue

g=nx.Graph()
g.add_nodes_from([1,2,3,4,5,6,7,8,9])
g.add_weighted_edges_from([(1,2,140),(1,9,75),(2,3,80),(2,7,99),(2,8,151),(8,9,71),
                           (3,4,146),(3,5,97),(4,5,138),(5,6,101),(6,7,211)])
pos=nx.circular_layout(g)
nx.draw(g, pos, with_labels=True)
heuristics={1:366, 2:253, 3:193, 4:160, 5:98, 6:0, 7:178, 8:380, 9:374}
#GBFS
def gbfs(source, heuristics, graph, goal):
  path=[]
  q=queue.PriorityQueue()
  q.put([heuristics,source])
  while(q.empty()==False):
    current=q.get()[1]
    path.append(current)
    q=queue.PriorityQueue()
    if(current==goal):
      break
    for i in graph.neighbors(current):
      if i not in path:
        q.put([heuristics[i],i])
  return path

#ASTAR
def astar(source, heuristics, graph, goal):
  path=[]
  distance=0
  q=queue.PriorityQueue()
  q.put((heuristics[source]+distance, [source,0]))
  while(q.empty()==False):
    current = q.get()[1]
    distance = current[1]
    q=queue.PriorityQueue()
    if(current==goal):
      break
    path.append(current[0])
    weight_edge_pairs = graph.edges(current[0], data=True)
    for j,i,weight in weight_edge_pairs:
      if i not in path:
        q.put((heuristics[i]+distance+weight['weight'],[i, distance]))
  return path

astar=astar(1, heuristics, g, 6)
print(astar)
astar_edge=[(astar[i],astar[i+1]) for i in range(0,len(astar)-1)]

gbfs = gbfs(1, heuristics, g, 6)
gbfs_edge = [(gbfs[i], gbfs[i+1]) for i in range(0, len(gbfs)-1)]

nx.draw(g, pos, edgelist=astar_edge, edge_color="wheat")
nx.draw(g, pos, edgelist=gbfs_edge, edge_color='pink')
print(gbfs)