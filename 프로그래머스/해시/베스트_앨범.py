def solution(genres, plays):
    genres_map = dict()

    for i in range(len(genres)):
        if genres[i] not in genres_map:
            genres_map[genres[i]] = {"total": plays[i], "values": {i: plays[i]}}
        else:
            genres_map[genres[i]]["total"] += plays[i]
            genres_map[genres[i]]["values"][i] = plays[i]

    sorted_genres = sorted(genres_map.items(), key=lambda item: -item[1]["total"])
    answer = []

    for value in sorted_genres:
        data = value[1]['values']
        sorted_data = sorted(data.items(), key=lambda item: (-item[1], item[0]))
        if len(sorted_data) >= 2:
            answer.append(sorted_data[0][0])
            answer.append(sorted_data[1][0])
        else:
            answer.append(sorted_data[0][0])
    return answer