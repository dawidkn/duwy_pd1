import numpy as np
import math
from connections import equation



def displacement(S, Q, Rot, eqN, extension, tracking, ismoving, time, step_time, connect, isground):
    # for i in eqN:
    # Jacobian(eqN, extension, Rot, Q, S)
    current_t = 0
    # print(tracking)
    # print(Rot)
    # print(Q)
    # print(S)
    # print(eqN)
    Fq = []
    while current_t < time:
        
        Fq = Jacobian(eqN, extension, Rot, Q, S, isground, ismoving, tracking)


        current_t += step_time
    print(Fq)

def Jacobian(eqN, extension, Rot, Q, S, isground, ismoving, tracking):
    om = np.array([[0, 1], [1, 0]])
    lm = int(len(eqN)+len(extension))
    Fq = np.zeros((lm, lm))
    position = 0


    
    for i in range((len(eqN)-len(ismoving))): #uzupelnianie jacobiego dla obrotowych
        
        if tracking[i][0] == 0:
            Fq[position:position+2, position:position+2] = np.eye(2)
            
            Fq[position:position+2, position:position+1] = om @ Rot[tracking[i][1]-1] @ S[i+1]

        else:
            Fq[position:position+2, position:position+2] = - np.eye(2)
            
            Fq[position:position+2, position+2] = (om @ Rot[tracking[i][1]-1] @ S[i+1])

        
        # position +=2
            
    return Fq
        # elif:
        #     print("test")
        


        

        