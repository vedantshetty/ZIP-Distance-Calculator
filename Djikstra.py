from collections import defaultdict
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}
		self.times = {}
		
#function to add graphs in a node
	def add_node(self, value):
		self.nodes.add(value)

#function to build edges in a graph
	def add_edge(self, from_node, to_node, distances,time):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		
		self.times[(from_node,to_node)] = time
		self.times[(to_node,from_node)] = time
		self.distances[(from_node, to_node)] = distances
		self.distances[(to_node,from_node)] = distances
		
		
def djikstra(graph, initial):
	visited = [{initial: 0}, {initial: 0}]
	#path = defaultdict(list)
	nodes = set(graph.nodes)
	while nodes: 
		min_node = None
		for node in nodes:
			if node in visited[0]:
				if min_node is None:
					min_node = node
				elif visited[0][node] < visited[0][min_node]:
					min_node = node
		if min_node is None:
			break
		nodes.remove(min_node)
		current_weight = visited[0][min_node]
		current_dis =visited[1][min_node]
		for edge in graph.edges[min_node]:
			weight = current_weight + graph.times[(min_node, edge)]
			total_distances = current_dis +  graph.distances[(min_node,edge)]
			
			if edge not in visited[0] or weight < visited[0][edge]:
				visited[0][edge] = weight
				visited[1][edge] = total_distances
				
				#path[edge].append(min_node)
	return visited
