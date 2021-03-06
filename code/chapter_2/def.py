# add라는 이름의 함수를 정의합니다.
# 이 함수는 매개변수로 a와 b를 받고 더한 뒤 반환합니다.
def add(a, b):
    return a + b  # return 구문으로 값을 반환합니다.

# 함수를 호출할 때는 함수 이름 뒤에 괄호를 입력하고
# 내부에 매개변수를 지정합니다.
print(add(1, 2))  # 3라고 출력합니다.

# <매개변수>=<값>이라는 형태로도 매개변수를 지정할 수 있습니다.
# 이를 키워드 매개변수라고 합니다.
print(add(1, b=3))  # 4라고 출력합니다.