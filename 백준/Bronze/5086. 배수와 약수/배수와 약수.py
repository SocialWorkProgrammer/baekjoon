# 해결전략 : 서로를 나눠 약수인지 배수인지 구하기
for i in range(10000): # 테스트 케이스의 개수를 모르기 때문에 우선 만 개로 설정
    a, b = map(int, input().split())
    if a == 0 and b == 0: # 만약 둘 다 0일 경우 for문을 종료시킴
        break
    else:
        if a % b == 0:
            print('multiple')
            continue
        elif b % a == 0:
            print('factor')
            continue
        else:
            print('neither')
            continue