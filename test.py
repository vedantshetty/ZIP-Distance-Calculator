import Djikstra
import csv
g = Djikstra.Graph()
nodelist = ["A","B","C","D","E","F","G"]
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')

g.add_edge('A','B',1,12)
g.add_edge('A','C',1,7)
g.add_edge('B','D',1,1)
g.add_edge('B','A',1,12)
g.add_edge('D','E',1,8)
g.add_edge('C','F',1,3)
g.add_edge('D','G',1,5)
g.add_edge('F','B',1,1)
g.add_edge('F','G',1,2)
g.add_edge('C','D',1,13)
g.add_edge('E','B',1,6)

with open("test.csv", "w", newline="") as output_file:
	writer = csv.writer(output_file, delimiter = ",")
	writer.writerow(["Source","Destination","Time", "Distance"])
	
for i in nodelist:
	data = Djikstra.djikstra(g,i)
	with open("test.csv", "a", newline = "") as output_file:
		writer = csv.writer(output_file,delimiter = ",")
		for key in data[0]:
			writer.writerow([i,key,data[0][key],data[1][key]])
