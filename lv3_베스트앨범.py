def solution(genres, plays):
    genres_sum = {}
    for genre, play in zip(genres, plays):
        if genre in genres_sum.keys():
            genres_sum[genre] += play
        else:
            genres_sum[genre] = play

    #print(genres_sum)

    info_dict = {}

    for idx, info in enumerate(zip(genres, plays)):
        genre, play_count = info[0], info[1]
        genre_count = genres_sum[genre]

        if genre in info_dict.keys():
            if len(info_dict[genre]) >= 2:
                info_dict[genre].append([genre_count, play_count, idx])
                info_dict[genre] = sorted(info_dict[genre], key=lambda x: -x[1])[:2]
            else:
                info_dict[genre].append([genre_count, play_count, idx])
        else:
            info_dict[genre] = [[genre_count, play_count, idx]]

    #print(info_dict)

    k = sum(info_dict.values(), [])
    kk = sorted(k, key=lambda x: (-x[0], -x[1], x[2]))
    #print(k)
    #print(kk)

    return [i[2]for i in kk]
