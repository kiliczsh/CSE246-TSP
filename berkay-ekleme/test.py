from readInput import Converter 
from nodes import Nodes
from numpy import sqrt
from algorihms import bfs,clear_repeats
from sys import argv

inputfile=argv[1] #'example-input-2.txt'
mapfile='map.txt'
outputfile='output.txt'
distancefile='distances.txt'

root_idx = 0

def init_nodes(locations):
    nodes = []
    for i in range(lnt):
        nodes.append(Nodes(locations[i][0],locations[i][1],i,lnt))
    for i in range(lnt):
        current_node=nodes[i]
        print("node",str(i),"'s distance sort started")
        for j in range(lnt):
            dst_sqr_x=(current_node.x-nodes[j].x)*(current_node.x-nodes[j].x)
            dst_sqr_y=(current_node.y-nodes[j].y)*(current_node.y-nodes[j].y)
            dst=sqrt(dst_sqr_x+dst_sqr_y)
            nodes[i].fill_distance(int(round(dst)),j)
    return nodes

def calc_lnt(nodes,path):
    total=0
    lnt = len(path)
    for i in range(lnt-1):
        total+=nodes[path[i]].find_distance(path[i+1])
    return total
print("start")
converter = Converter(inputfile,mapfile,outputfile)

locations = converter.read_and_convert()
lnt = len(locations)

nodes=init_nodes(locations)


for i in range(len(nodes)):
    nodes[i].sort_distances()
    print("node",str(i),"'s distances sorted")

dstfile = open(distancefile, 'w')

for i in range(len(nodes)):
    nodes[i].save_distances(dstfile)
    dstfile.write('\n')

dstfile.close()

save=bfs(nodes,root_idx)
print(save)
save=clear_repeats(nodes,save)
lnt_path=calc_lnt(nodes,save)
converter.save_output(lnt_path,save)
converter.finish()