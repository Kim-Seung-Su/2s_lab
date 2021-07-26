def decorator(func): # 인자로 함수,func를 받음
    def decorated():
        print('함수시작')
        func()
        print('함수끝')
    return decorated

@decorator
def hello_world():
    print('Hello World')

hello_world()
