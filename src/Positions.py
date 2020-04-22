def zero_0(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
   
    #n : int
    n = N-2 
    
    for i in range(1,25):
        # list : list[int]
        list = []
        
            
        if i >= 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+c and j>=(13+int(d/2))-c:
                    list.append(1)
                else:
                    list.append(0)
               
            if c < n-1:     
                c = c+1        
        else:
            for j in range(1,25):
                list.append(0)
                            
        monde.append(list)
                
    return monde


def zero_90(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
    
        if i < 24-((3*n)-2+n):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
                
        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
            if e < n-1:     
                e = e+1 
            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 
                            
            monde.append(list)
        
    return monde
        

def zero_180(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    #f : int
    f = n-1
    
    for i in range(1,25):
        # list : list[int]
        list = []
    
        if i < 24-((6*n)-4):
            for j in range(1,25):
                list.append(0)
            monde.append(list)

        elif i < 24-(4*n-2):
            for j in range(1,25):
                if j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            monde.append(list)

        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            if f > 0:
                f = f-1
            monde.append(list)


        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)

            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 

            monde.append(list)
        
    return monde

def quatre_vingts_dix_0(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
    
        if i < 24-((3*n)-2+n):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
                
        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                else:
                    list.append(0)
            if c < n-1:     
                c = c+1 
            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 
                            
            monde.append(list)
        
    return monde

def quatre_vingts_dix_90(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
    
        if i < 24-((3*n)-2+n):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
                
        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
            if c < n-1:     
                c = c+1 
            if e < n-1:     
                e = e+1 
            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 
                            
            monde.append(list)
        
    return monde

def quatre_vingts_dix_180(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    #f : int
    f = n-1
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
        
        if i < 24-((6*n)-4):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
            
        elif i < 24-(4*n-2):
            for j in range(1,25):
                if j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            monde.append(list)

        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                elif j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                else:
                    list.append(0)
            if f > 0:
                f = f-1        
            if c < n-1:     
                c = c+1 

            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 
                            
            monde.append(list)
        
    return monde

def cent_quatre_vingts_0(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    #f : int
    f = n-1
    
    for i in range(1,25):
        # list : list[int]
        list = []
    
        if i < 24-((6*n)-4):
            for j in range(1,25):
                list.append(0)
            monde.append(list)

        elif i < 24-(4*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            monde.append(list)

        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            if f > 0:
                f = f-1
            monde.append(list)


        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)

            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 

            monde.append(list)
        
    return monde


def cent_quatre_vingts_90(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #e : int
    e = 0
    #n : int
    n = N-2
    #f : int
    f = n-1
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
        
        if i < 24-((6*n)-4):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
            
        elif i < 24-(4*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            monde.append(list)

        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
            if f > 0:
                f = f-1        
            if e < n-1:     
                e = e+1 

            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+e and j>=(13+int(d/2))-e:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
            if e < n-1:     
                e = e+1 
                            
            monde.append(list)
        
    return monde

def cent_quatre_vingts_180(D,N):
    
    
    d = D/2.5
    #monde : list[list[int]]
    monde = []
    #c : int
    c = 0
    #n : int
    n = N-2
    #f : int
    f = n-1
    
    
    for i in range(1,25):
        # list : list[int]
        list = []
        
        if i < 24-((6*n)-4):
            for j in range(1,25):
                list.append(0)
            monde.append(list)
            
        elif i < 24-(4*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                elif j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            monde.append(list)

        elif i < 24-(3*n-2):
            for j in range(1,25):
                if j <=(12-int(d/2))+f and j>=(12-int(d/2))-f:
                    list.append(1)
                elif j <=(13+int(d/2))+f and j>=(13+int(d/2))-f:
                    list.append(1)
                else:
                    list.append(0)
            if f > 0:
                f = f-1        
            

            monde.append(list)
                
        else:
            for j in range(1,25):
                if j <=(12-int(d/2))+c and j>=(12-int(d/2))-c:
                    list.append(1)
                elif j <=(13+int(d/2))+c and j>=(13+int(d/2))-c:
                    list.append(1)
                else:
                    list.append(0)
                
            if c < n-1:     
                c = c+1
                            
            monde.append(list)
        
    return monde
