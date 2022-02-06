import sys
from collections import deque
input = sys.stdin.readline
N,T = map(int,input().split())
 
turns = list(map(int,input().split()))
 
 
 
card_deck = deque()
 
for _ in range(T):
    temp = input().rstrip().split(' ')
    card_deck.append(temp)
 
occupy_card = [[] for _ in range(N+2)]
result = []
used_card_num = set()
for i in range(T):
    person = turns[i]
 
    if len(occupy_card[person])>0:
        card_num,wanted_num = occupy_card[person]
        result.append(card_num)
        if wanted_num in used_card_num:
            continue
        else:
            used_card_num.add(wanted_num)
            occupy_card[person] = []
    else:
        card_num,rests= card_deck.popleft()
        result.append(card_num)
        if rests[0] == 'next':
            continue
        elif rests[0] == 'acquire':
            if rests[1] in used_card_num:
                occupy_card[person] = (card_num,rests[1])
            else:
                used_card_num.add(rests[1])
        elif rests[0] == 'release':
            used_card_num.remove(rests[1])
 
 
for i in range(T):
    sys.stdout.write(result[i]+'\n')