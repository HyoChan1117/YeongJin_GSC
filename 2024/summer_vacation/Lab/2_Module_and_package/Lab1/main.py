
import utilities

def main():
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    operation = input("연산자를 고르세요 (add, subtract, multiply, divide): ")
    
    if operation == 'add':
        result = utilities.add(num1, num2)
    elif operation == 'subtract':
        result = utilities.subtract(num1, num2)
    elif operation == 'multiply':
        result = utilities.multiply(num1, num2)
    elif operation == 'divide':
        result = utilities.divide(num1, num2)
    else:
        print("사용할 수 없는 연산자입니다.")
        return
    
    print(f"결과: {result}")
    
if __name__ == '__main__':
    main()