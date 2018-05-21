def bfs(nodes,root_idx):
    stack=[]
    save=[]
    prev_dist=10000000000
    current_idx=root_idx
    while True:
        save.append(current_idx)
        print("bfs:",str(current_idx))
        
        if(nodes[root_idx].is_finished): break
        while True:
            repeat=False
            next_idx = nodes[current_idx].show_next(prev_dist)
            for i in save:
                if i==next_idx:
                    repeat=True
            if repeat and not (nodes[current_idx].is_finished):
                continue
            elif not (nodes[next_idx].is_finished):
                if next_idx!=0:
                    stack.append(current_idx)
                    current_idx = next_idx
                else:
                    current_idx = stack.pop()
                break
            elif nodes[current_idx].is_finished:
                save.pop()
                break
    return save

def clear_repeats(nodes,path):
    lnt = len(path)
    for i in range(lnt):
        for j in range(i+1,len(path)-1):
            mid=-1
            print("clear: ", str(i),str(j),str(len(path)))
            if path[j]==path[i]:
                if i == 0 and j!=lnt-1: 
                    path[j] = -1
                    mid=j
                elif j==lnt-1 and i!=0:
                    path[i] = -1
                    mid=i
                elif j==lnt-1 and i==0:
                    continue
                else:
                    dist_first_pass = nodes[path[i-1]].find_distance(path[i+1])
                    dist_second_pass = nodes[path[j+1]].find_distance(path[j+1])
                    dist_first_normal = nodes[path[i-1]].find_distance(path[i])+nodes[path[i]].find_distance(path[i+1])
                    dist_second_normal = nodes[path[j-1]].find_distance(path[j]) +nodes[path[j]].find_distance(path[j+1])
                    
                    eff_first = dist_first_normal-dist_first_pass
                    eff_second = dist_second_normal-dist_second_pass

                    if(eff_first>=eff_second):
                        path[i]=-1
                        mid=i
                    else:
                        path[j]=-1
                        mid=j
                if(mid!=-1):
                    first_part=path[0:mid]
                    second_part=path[mid+1:lnt]
                    path=first_part+second_part
                    print(first_part,second_part)
                    lnt=len(path)                
    return path
