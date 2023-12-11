import sys

def get_dist(mbti1, mbti2):
    dist = 0
    for i in range(len(mbti1)):
        if mbti1[i] != mbti2[i]:
            dist += 1

    return dist


mbti = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
mbti_index = dict()
# 두 mbti 사이의 거리
mbti_dist = [[0 for _ in range(len(mbti))] for _ in range(len(mbti))]

for i in range(len(mbti)):
    mbti_index[mbti[i]] = i

for i in range(len(mbti)):
    for j in range(i, len(mbti)):
        mbti_dist[i][j] = get_dist(mbti[i], mbti[j])
        mbti_dist[j][i] = mbti_dist[i][j]


for _ in range(int(input())):
    N = int(input())
    student_mbti = list(sys.stdin.readline().split())
    max_dup_count = 1

    student_dict = dict()
    # 2개 중복되는 mbti를 모아둔다.
    two_dup = []

    # 중복되는 mbti가 있는지 체크한다.
    for i in range(len(student_mbti)):
        if student_mbti[i] not in student_dict:
            student_dict[student_mbti[i]] = 1
        else:
            student_dict[student_mbti[i]] += 1
            max_dup_count = max(max_dup_count, student_dict[student_mbti[i]])
            # mbti가 3개 이상 중복된 경우에는 거리가 3 mbti 사이의 최소 거리는 0이된다.
            if max_dup_count == 3:
                break
            else:
                two_dup.append(student_mbti[i])

    answer = 32

    # mbti가 3개 중복되는 경우에는 최소 거리는 0이다.
    if max_dup_count == 3:
        print(0)
    # mbti가 2개 중복되는 경우에는 3개의 mbti 중 2개를 중복되는 mbti를 선택하는 경우도 고려해야한다.
    elif max_dup_count == 2:
        student_mbti = list(set(student_mbti))
        # 서로다른 mbti 3개 선택하는 경우
        for i in range(len(student_mbti)):
            for j in range(i+1, len(student_mbti)):
                for k in range(j+1, len(student_mbti)):

                    answer = min(answer, mbti_dist[mbti_index[student_mbti[i]]][mbti_index[student_mbti[j]]]
                                 + mbti_dist[mbti_index[student_mbti[j]]][mbti_index[student_mbti[k]]]
                                 + mbti_dist[mbti_index[student_mbti[k]]][mbti_index[student_mbti[i]]])

        # 중복되는 mbti 2개, 다른 mbti 1개를 선택하는 경우
        for i in range(len(student_mbti)):
            for j in range(len(two_dup)):
                if student_mbti[i] != two_dup[j]:
                    answer = min(answer, 2 * mbti_dist[mbti_index[student_mbti[i]]][mbti_index[two_dup[j]]])

        print(answer)

    # 중복되는 mbti가 단 한개도 없기 때문에 서로다른 mbti를 3개 골라서 최소 거리를 구한다.
    else:
        student_mbti = list(set(student_mbti))
        for i in range(len(student_mbti)):
            for j in range(i+1, len(student_mbti)):
                for k in range(j+1, len(student_mbti)):

                    answer = min(answer, mbti_dist[mbti_index[student_mbti[i]]][mbti_index[student_mbti[j]]]
                                 + mbti_dist[mbti_index[student_mbti[j]]][mbti_index[student_mbti[k]]]
                                 + mbti_dist[mbti_index[student_mbti[k]]][mbti_index[student_mbti[i]]])

        print(answer)
