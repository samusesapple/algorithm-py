# 문제 1. 정수 두 개를 입력받아 합을 출력하라.
num_a, num_b = map(int, input().split())
print(num_a+num_b)


# 문제 2. 문자열 하나를 입력받아 뒤집어서 출력하라.

    ## 3위 - 반복문 사용
def solution_loop(s):
    answer = ''
    for i in s:
        answer = i + answer    
    print(answer)
    
    ## 1위 - 슬라이싱 사용 > 문자열[시작:끝:간격] - 간격을 -1 <- 
def solution_slicing(s):
    answer = s[::-1]
    print(answer)

    ## 2위- 내장함수 reversed사용 - reversed(문자열)의 return 값은 iterator이기에 ''.join을 이용하여 문자열로 변환 필요
def solution_reversed(s):
    iterator_str = reversed(s)
    answer = ''.join(iterator_str)
    print(answer)


# 문제 3. 공백으로 구분된 숫자들(길이 모름)의 평균 구하기
num_list = list(map(int, input().split())) # input을 띄어쓰기 기준으로 하나씩 int형태의 list로 변경
print(sum(num_list) // len(num_list)) # list의 총합 나누기 list의 길이 (나머지 제거)

# 문제 4. 문장을 입력 받고, 띄어쓰기 기준으로 단어가 몇 개인지 출력하라.
sentence = input().strip() # 문장 끝 \n문자열 제거한 문장 받기
word_list = sentence.split() # 띄어쓰기 기준으로 문자들을 받아 배열로 변경
print(len(word_list))

# 문제 5. 정수 여러개를 입력받아 그 중 가장 큰 값을 출력하라.
nums = list(map(int, input().split()))
print(max(nums)) # iterable(대소비교 가능)한 list 중 가장 큰 값을 뽑아줌