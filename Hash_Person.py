# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# 이중포문 사용 ==> 효율성이 낮음 (50점) ------------------------------------------------------------------------------------
# def solution(participant, completion):
#
#     participant.sort() # 동명이인 문제를 해결하기위해 정렬
#     completion.sort()
#
#     for i in range(len(completion)):
#         for j in range(len(participant)):
#             if completion[i] == participant[j]:
#                 participant.pop(j)
#                 break
#     return participant.pop()

# def solution(participant, completion): # 이경우는 무조건 완주못한사람이 한명일 경우에만 해당됨 ==> 단일포문으로 시간복잡도 해결
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[len(participant)-1]
#
#
#
#
# participant = ["leo","kiki","eden"]
# completion = ["eden","kiki" ]
# print(solution(participant, completion))

# zip 사용   ------------------------------------------------------------------------------------------------------------
# def solution(participant, completion):
#
#
#     participant.sort()
#     completion.sort()
#
#     for par, com in zip(participant, completion):
#         if par != com:
#             return par
#     return participant.pop()
#
# participant = ["leo","kiki","eden"]
# completion = ["kiki","eden" ]
#
# print(solution(participant, completion))


# 컬렉션 사용 ------------------------------------------------------------------------------------------------------------
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # 차집함을 쓰기위해 컬렉션 사용
    return list(answer)[0]

participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]

print(solution(participant, completion))