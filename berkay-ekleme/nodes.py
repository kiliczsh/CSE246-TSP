

class Nodes:
    points=0
    is_finished=False
    def __init__(self,x,y,idx,lnt):
        print("node",idx,"initialized")
        self.x=x
        self.y=y
        self.distances=[[None,None]]*lnt
        self.dst_lnt = len(self.distances)
        self.idx=idx

    def fill_distance(self,distance,idx):
        self.distances[idx]=[distance,idx]
    
    def sort_distances(self):
        self.distances=sorted(self.distances)

    def save_distances(self,save_file):
        lnt = len(self.distances)
        save_file.write('[')
        for i in range(lnt):
            save_file.write(str(self.distances[i])+' ')
        save_file.write(']')
    
    def show_next(self,prev_dst):
        if prev_dst < self.distances[self.points][1]: return 0
        elif self.points<self.dst_lnt-1: self.points+=1
        else:
            self.is_finished=True
            return 0
        return self.distances[self.points][1]
    
    def find_distance(self,idx):
        lnt = len(self.distances)
        for i in range(lnt):
            if self.distances[i][1]==idx:
                return self.distances[i][0]
        return -1