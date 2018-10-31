import csv
import Djikstra
g= Djikstra.Graph()

#loading vertices into the graph
def loadnode(filename = "1.csv"):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file,delimiter = ",")
		for row in csv_reader:g.add_node(row[0])
		return
		
#loading edges into the graph
def loadpaths(filename = "Adjacency_Matrix.csv"):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter= ",")
		for row in csv_reader:
			g.add_edge(row[0],row[1],int(row[2]),int(row[3]))
	
def findtimes(filename = "Full_ZIP_List.csv"):
	outputfile = "output.csv"
	data = []
	
	#Building headers
	with open(outputfile, "w",newline= "") as output_file:
		writer = csv.writer(output_file, delimiter =",")
		writer.writerow(["Source ZIP","Destination ZIP", "Time", "Distance"])
		
	with open(filename) as csv_file:
		csv_reader = csv_reader(csv_file,delimiter = ",")
		for row in csv_reader:
			zip = row[0]
			data = Djikstra.djikstra(g,zip)
		
		#Writing Data
		with open(outputfile,"a",newline="") as output_file:
			writer.writerow([zip,key,data[0][key],data[1][key])
		
			
loadnode()
loadpath()
findtimes()
