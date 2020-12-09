def solution(pn):
    pn_list=list(pn)
    for i in range(len(pn)-4):
        pn_list[i]= "*"

    return "".join(pn_list)