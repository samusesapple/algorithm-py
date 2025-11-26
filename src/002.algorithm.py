# Day2 실습 문제

# 정수 n을 입력받아 아래 규칙대로 출력하라.

# 조건:
# 	1.	1부터 n까지 숫자를 한 줄씩 출력한다.
# 	2.	단,
# 	•	숫자가 3의 배수이면 “Fizz”
# 	•	숫자가 5의 배수이면 “Buzz”
# 	•	숫자가 3과 5의 공통 배수이면 “FizzBuzz”
# 	•	그 외 숫자는 숫자 그대로 출력한다.
# 	3.	반복문은 for 또는 while 아무거나 사용 가능.

n = int(input())
for num in range(1, n+1):
    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
