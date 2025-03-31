class Foo {
    // 1) 멤버변수
    //     A. 인스턴스 멤버 변수
    //     B. 클래스 멤버 변수
    // 2) 지역변수 -> 메서드 내 선언된 변수
}

class Bar {
    int x;
    String y;
    boolean z;

    void prt() {
        // 지역변수는 임시적으로 저장하기 위해 사용
        // Block({}) 단위로 생성
        // 지역변수를 선언할 때 지역변수는 자동으로 초기화 되지 않음
        
        // 지역변수는 어디에서 쓰일까?
        // 1. 메서드
        // 2. 초기화 블록
        // 3. 생성자

        {
            int a = 3;
            {
                System.out.println(a);
                int b = 5;
            }

            int sum = 0;
            for (int i = 0 ; i < 5 ; i++) {
                sum += i;
            }

            System.out.println(sum);
        }

        // System.out.println(a + ":" + this.x);

        // 찾아가는 순서
        // 1. 현재 블럭 뒤지기
        // 2. 현재 객체
    }
}

public class test {
    public static void main(String[] args) {
        // 객체 생성
        (new Bar()).prt();


    }
}
