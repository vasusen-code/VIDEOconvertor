#Tg:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

def two_trial_queue(id, List1, List2):
    if not f'{id}' in List1:
        List1.append(f'{id}')
    else:
        return False
 
#Not in use
def two_trial_queue(id, List1, List2):
    if not f'{id}' in List1:
        List1.append(f'{id}')
    else:
        if not f'{id}' in List2:
            List2.append(f'{id}')
        else:
            return False

#Not in use        
def ps_queue(id, media, List1, List2):
    List1.append(f'{id}')
    List2.append(media)
    if not len(List1) < 2:
        return 'EMPTY'
    if len(List1) > 2:
        return 'FULL'
