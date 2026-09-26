def solution(spell, dic):
    dic_spell = [list(word) for word in dic]

    answer = 2
    for i in range(len(dic)):
        if set(spell) == set(dic_spell[i]):
            answer = 1
            break
        else:
            continue
    return answer