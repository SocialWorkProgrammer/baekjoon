Croatian = input()
cnt = 0
alphabetlist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alpha in alphabetlist:
    if alpha in Croatian:
        nums = Croatian.count(alpha)
        cnt += nums
        for i in range(nums):
            Croatian = Croatian.replace(alpha, '1')
        # 여기서 왜 안 없어지지?
        # 이유 : replace 메서드는 문자열을 직접 변경하지 않고 변경된 새로운 문자열을 반환하기 때문.
        # 따라서 새로운 문자열을 담을 변수를 만들어야 한다!!
    else:
        pass
print(len(Croatian))