# 문제
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

N=int(int(input()))
for i in range(1,N+1):
    print(i)


# comprehension 표현식

# [ 출력 표현식 for iterable자료 요소 in iterable자료형 ] 

[print(i) for i in range (1,(int(input())+1))]
