# word가 그룹 단어인지를 반환한다.
def is_group(word):
    # 매 루프를 돌면서 word의 가장 앞 문자를 c라고 하자.
    # 이때 c의 개수를 구해서, 해당 개수만큼 연속된 c를 제거해 본다. 만약 제거되지 않았다면 c가 떨어져 있다는 것을 의미한다.
    while len(word) > 0:
        old_len = len(word)  # 제거하기 전의 길이
        num_of_first = word.count(word[0])  # 맨 앞 문자의 개수

        # 맨 앞 문자가 num_of_first만큼 연속된 문자를 제거하려고 시도해본다.
        word = word.replace(word[0]*num_of_first, '')
        new_len = len(word)  # 제거한 후의 길이

        # 제거가 되지 않았다면 루프를 빠져나온다.
        if new_len == old_len:
            break

    # while문을 모두 수행 후에 남아있는 문자가 있다면, 이는 그룹문자가 아닌 것을 의미한다. 따라서 word가 비어있는지를 리턴한다.
    return len(word) == 0


N, *words = open(0).read().split()

answer = list(filter(lambda w: is_group(w), words))
print(len(answer))
