class ListPlus(list):
    def __add__(self, other):
        li1_tmp=self.copy() 
        li2_tmp=other.copy()
    
        if len(self) < len(other):
            li1_tmp.extend([0]*(len(other)-len(self)))
        
        elif len(other) < len(self):
            li2_tmp.extend([0]*(len(self)-len(other)))   
        
        res=ListPlus()
        for i in range(len(li1_tmp)):
            res.append(li1_tmp[i]+li2_tmp[i])
   
        return res
    
if __name__ == '__main__':
    
    l1=ListPlus([3,4,5,6])
    l2=ListPlus([3,4])
    l2.append(5)
    l3=l1+l2
    print(l3, type(l3)) # output should be [6,8,10,6]