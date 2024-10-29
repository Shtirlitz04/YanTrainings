t_room, t_cond = map(int, input().split())
reg = str(input())
if reg == 'heat':
    if t_cond >= t_room:
        print(t_cond)
    else:
        print(t_room)
elif reg == 'freeze':
    if t_cond <= t_room:
        print(t_cond)
    else:
        print(t_room)
elif reg == 'auto':
    print(t_cond)
elif reg == 'fan':
    print(t_room)
