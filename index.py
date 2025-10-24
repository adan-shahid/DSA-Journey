competitors = ['A', 'B', 'C', 'D']
power = [42750, 31645, 12455, 12455]

while len(competitors) > 1:
    next_round = []
    next_power = []
    for i in range(0, len(competitors), 2):
        fighter1, power1 = competitors[i], power[i]
        fighter2, power2 = competitors[i+1], power[i+1]

        if power1 > power2:
            power1 += power2
            win_name, win_power = fighter1, power1

        elif power2 > power1:
            power2 += power1
            win_name, win_power = fighter2, power2
        else:
            win_power = power1 + power2
            win_name = fighter1 + fighter2

        next_round.append(win_name)
        next_power.append(win_power)
        
    competitors = next_round
    power = next_power    
    
print(win_name)



