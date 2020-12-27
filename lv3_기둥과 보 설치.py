def check(answer):
    for x, y, cate in answer:
        if cate == 0:   #기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False

        elif cate == 1:     #보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, cate, ox = frame

        if ox == 1:
            answer.append([x, y, cate])
            if check(answer) == False:
                answer.remove([x, y, cate])

        elif ox == 0:
            answer.remove([x, y, cate])
            if check(answer) == False:
                answer.append(([x, y, cate]))

    return answer.sort()
