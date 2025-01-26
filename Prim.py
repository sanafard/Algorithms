#Prim’s algorithm to find the Minimum Spanning Tree (MST) of a graph represented as an adjacency list
# O((V+E)logV) 
class Node:
    def __init__(self,k,v):
        self.key=k #cost to node
        self.value=v #related edge

    def __lt__(self, other):
        return self.key< other.key

class PriorityQueue:   #heap
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def parent(self,j):
        return (j-1)//2
    def right(self,j):
        return 2*j+2
    def left(self,j):
        return 2*j+1
    def has_left(self,j):
        return self.left(j) < len(self)
    def has_right(self,j):
        return self.right(j)< len(self)
    def swap(self,i,j):
        self.data[i], self.data[j]=self.data[j] , self.data[i]
    def upheap(self,j):
        parent=self.parent(j)
        if j>0 and self.data[j]<self.data[parent]:
            self.swap(j,parent)
            self.upheap(parent)

    def downheap(self,j):
        if self.has_left(j):
            left=self.left(j)
            small_child=left
            if self.has_right(j):
                right=self.right(j)
                if self.data[right]<self.data[left]:
                    small_child=right
            if self.data[small_child]<self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    def add(self,key , value):
        token=Node(key,value)
        self.data.append(token)
        self.upheap(len(self.data)-1)
        return token

    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        self.swap(0, len(self.data)-1)
        item=self.data.pop()
        self.downheap(0)
        return item.key , item.value

    def update(self,loc,new_key,new_val):
        loc.key=new_key
        loc.value=new_val
        j=self.data.index(loc)
        pj=self.parent(j)
        if j>0 and self.data[j]<self.data[pj]:
            self.upheap(j)   #check above j
        else:   #up is ok,look below j
            self.downheap(j)


def prim(adj_lst):
    all_cost=0
    mst=[]  #final solution
    pq=PriorityQueue()  #(cost to node,edge)
    pq_locater={}   #{node: 'node_instance in pq'},for fast accessing
    for v in adj_lst :   #add vertices to available_nodes, one is randomly cost=0 to be the first node
        cost=0 if len(pq_locater)==0 else float('inf')
        new_node=pq.add(cost,(None,v))  #inplace also returns
        pq_locater[v]=new_node
    while not pq.is_empty():
        cost , edge = pq.remove_min()
        all_cost+=cost
        n1,n2=edge
        mst.append(f'{n1}-->{n2}')
        del pq_locater[n2]
        for v , w in adj_lst[n2].items():
            if v in pq_locater and w< pq_locater[v].key:
                pq.update(pq_locater[v] , w , (n2,v))
    return all_cost,mst[1:]

adj_lst={'A':{'B':2 , 'C':4},
         'B':{'A':2,'C':1 , 'D':1 , 'E':8},
         'C':{'A':4 , 'B':1 , 'E':8},
         'D':{'B':1 , 'C':8 , 'F':2},
         'F':{'D':7 , 'E':2}}

print(prim(adj_lst))
