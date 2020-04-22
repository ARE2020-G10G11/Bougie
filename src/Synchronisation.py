def en_phase(D,N,position1):
    #position1 la position de la bougie de gauche
    
 
    c = position1
    list = []
    
    for i in range(10):
        
        if c == 0:
            list.append(zero_0(D,N))
            list.append(zero_0(D,N))
            c = c + 90
        elif c == 90:
            list.append(quatre_vingts_dix_90(D,N))
            list.append(quatre_vingts_dix_90(D,N))
            c = c + 90
        elif c == 180:
            list.append(cent_quatre_vingts_180(D,N))
            list.append(cent_quatre_vingts_180(D,N))
            c = c + 90
        else:
            list.append(quatre_vingts_dix_90(D,N))
            list.append(quatre_vingts_dix_90(D,N))
            c = 0
    return list
        
        
def opposition_de_phase(D,N,position1):
    
    c = position1
    list = []
    
    for i in range(20):
        
        if c == 0:
            list.append(zero_180(D,N))
            list.append(zero_180(D,N))
            c = c + 90
        elif c == 90:
            list.append(quatre_vingts_dix_90(D,N))
            list.append(quatre_vingts_dix_90(D,N))
            c = c + 90
        elif c == 180:
            list.append(cent_quatre_vingts_0(D,N))
            list.append(cent_quatre_vingts_0(D,N))
            c = c + 90
        else:
            list.append(quatre_vingts_dix_90(D,N))
            list.append(quatre_vingts_dix_90(D,N))
            c = 0
    return list
        
        
def non_synchronisation(D,N,position1,position2):

    c1 = position1
    c2 = position2
    list = []
    
    for i in range(10):
        if c1 == 0:
            if c2 == 0:
                list.append(zero_0(D,N))
                list.append(zero_0(D,N))
            elif c2 == 90 or c2 == 270:
                list.append(zero_90(D,N))
                list.append(zero_90(D,N))
            elif c2 == 180:
                list.append(zero_180(D,N))
                list.append(zero_180(D,N))
            if c2 == 270:
                c2 = 0
            else:
                c2 = c2 + 90
            c1 = c1 + 90
        
        elif c1 == 90 or c1 == 270:
            if c2 == 0:
                list.append(quatre_vingts_dix_0(D,N))
                list.append(quatre_vingts_dix_0(D,N))
            elif c2 == 90 or c2 == 270:
                list.append(quatre_vingts_dix_90(D,N))
                list.append(quatre_vingts_dix_90(D,N))
            elif c2 == 180:
                list.append(quatre_vingts_dix_180(D,N))
                list.append(quatre_vingts_dix_180(D,N))
            if c2 == 270:
                c2 = 0
            else:
                c2 = c2 + 90
            if c1 == 270:
                c1 = 0
            else:
                c1 = c1 + 90
        else:
            if c2 == 0:
                list.append(cent_quatre_vingts_0(D,N))
                list.append(cent_quatre_vingts_0(D,N))
            elif c2 == 90 or c2 == 270:
                list.append(cent_quatre_vingts_90(D,N))
                list.append(cent_quatre_vingts_90(D,N))
            elif c2 == 180:
                list.append(cent_quatre_vingts_180(D,N))
                list.append(cent_quatre_vingts_180(D,N))
            if c2 == 270:
                c2 = 0
            else:
                c2 = c2 + 90
            c1 = c1 + 90
        
    return list
            
                
    
def synchronisation(D,N,p):
    
    d = D/2.5
    position1 = 0
    position2 = p
    a = 0
    b = 0
    mondes = []
    
    if d <= 7.5:
        mondes.append(etats(D,N,position1,position2))
        while (position1 != position2) and (a<10):
            if (a%1==0):
                if position1 == 270:
                    position1 = 0
                else:
                    position1 = position1+90
            if (b%1.5 == 0):
                if position2 == 270:
                    position2 = 0
                else:
                    position2 = position2+90
            a = a + 0.5
            b = b + 0.5
            mondes.append(etats(D,N,position1,position2))
        mondes = mondes + en_phase(D,N,position1)
        
    elif d<= 12.5:
        
        mondes.append(etats(D,N,position1,position2))
        while (abs(position1-position2) != 180) and (a<30):
            if (a%1==0):
                if position1 == 270:
                    position1 = 0
                else:
                    position1 = position1+90
            if (b%1.5 == 0):
                if position2 == 270:
                    position2 = 0
                else:
                    position2 = position2+90
            a = a + 0.5
            b = b + 0.5
            mondes.append(etats(D,N,position1,position2))
        mondes = mondes + opposition_de_phase(D,N,position1)
        
    else:
        mondes = non_synchronisation(D,N,position1,position2)
    
    return mondes
