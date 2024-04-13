import sys
sys.setrecursionlimit = 10**8
input = lambda: sys.stdin.readline().strip()

N, Q = map(int, input().split())
query = list(map(int, input().split()))
cmd, parents, authorities = query[0], query[1:N+1], query[N+1:N*2 + 1]
alerts = [True for _ in range(N + 1)]
answers = [0 for _ in range(N + 1)]

def update_count_recursive(c, power, alert):
    global answers
    if not alert:
        return
    answers[c] += 1
    if (power == 0) or (c == 0):
        return
    update_count_recursive(parents[c-1], power - 1, alerts[c])

def calc_count_can_alert_chat_room():
    global answers
    answers = [0 for _ in range(N + 1)]
    for c in range(1, N + 1):
        power = authorities[c-1]
        update_count_recursive(parents[c-1], power-1, alerts[c])
        

def set_alert(args):
    global alerts
    c = args[0]
    alerts[c] = not alerts[c]

def set_authority(args):
    global authorities
    c, power = args[0], args[1]
    authorities[c-1] = power

def set_parent(args):
    global parents
    c1, c2 = args[0] - 1, args[1] - 1
    tmp = parents[c1]
    parents[c1] = parents[c2]
    parents[c2] = tmp

def get_count_can_alert_chat_room(args):
    c = args[0]
    return answers[c]

def controller(cmd, args, is_updated):
    if cmd == 200:
        set_alert(args)
        is_updated = False
    elif cmd == 300:
        set_authority(args)
        is_updated = False
    elif cmd == 400:
        set_parent(args)
        is_updated = False
    elif cmd == 500:
        if not is_updated:
            calc_count_can_alert_chat_room()
            is_updated = True
        print(get_count_can_alert_chat_room(args))


if __name__=="__main__":
    is_updated = False
    for _ in range(Q - 1):
        query = list(map(int, input().split()))
        cmd, args = query[0], query[1:]
        controller(cmd, args, is_updated)