def isValidIP(IPString):

    #Bigger than 3 number
    if(len(IPString)==0 or len(IPString)>3):
        return False
    #Leading zero's
    if(IPString[0] == '0' and len(IPString)>1):
        return False
    #Out of range [0, 255]
    if(not (0 <=int(IPString) <= 255)):
        return False
    return True



def restoreIPS(IPstring:str, start:int , curr_list, remainingToCompleteIP, all_lists):

    if(remainingToCompleteIP == 1):
        if (isValidIP(IPstring[start:])):
            curr_list.append(IPstring[start:])
            all_lists.append(curr_list.copy())
            curr_list.pop()
            return
    else:
        for i in range (start+1,start+4):
            if( isValidIP(IPstring[start: i]) and remainingToCompleteIP*3 >= len(IPstring[start:])):
                curr_list.append(IPstring[start: i])
                restoreIPS(IPstring,i, curr_list,remainingToCompleteIP-1, all_lists)
                curr_list.pop()

#Driver Code
s = "88883456"
all_lists= []
restoreIPS(s,0,[], 4, all_lists)
print(all_lists)