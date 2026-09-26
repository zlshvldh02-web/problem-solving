from collections import Counter

def solution(friends, gifts):
    
    # 선물 개수 정리
    count = Counter(gifts)
    gift_table = [[count[f"{a} {b}"] for b in friends] for a in friends]
    
    # 선물 지수 정리
    gift_score = []
    for i in range(len(friends)):
        give = sum(gift_table[i])
        recieve = sum(gift_table[j][i] for j in range(len(friends)))
        gift_score.append(give-recieve)
            
    # 선물 관계 정리
    result = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            difference = gift_table[i][j] - gift_table[j][i]
            if difference > 0:
                result[i] += 1
            elif difference < 0:
                result[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    result[i] += 1
                elif gift_score[i] < gift_score[j]:
                    result[j] += 1
                else:
                     continue
            
    answer = max(result)
    
    return answer