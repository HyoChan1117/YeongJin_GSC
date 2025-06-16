package learningContents.component.nestedClass.innerClass.localInnerClass;

class OuterClass {
    // 외부 클래스의 인스턴스 변수
    private int outerVar = 20;  // LocalInner 클래스에서도 접근 가능

    // 외부 클래스의 메서드
    void outerMethod(final int methodParam) {
        // 외부 메서드의 지역 변수
        final int localVar = 10; // LocalInner에서 사용되므로 final (또는 effectively final)

        // --- 지역 내부 클래스 (Local Inner Class) 선언 ---
        class LocalInner {
            // 지역 내부 클래스의 인스턴스 변수
            private String innerVar = "내부 변수";

            // 지역 내부 클래스의 메서드
            void display() {
                System.out.println("--- LocalInner.display() 호출 ---");

                // 1. 외부 클래스의 멤버 접근
                System.out.println("OuterClass의 outerVar: " + outerVar);
                System.out.println("OuterClass의 this 참조: " + OuterClass.this.outerVar);

                // 2. 자신을 감싸는 메소드의 매개변수 및 지역 변수 접근 (final 또는 effectively final이어야 함)
                System.out.println("외부 메소드의 파라미터 (methodParam): " + methodParam);
                System.out.println("외부 메소드의 지역 변수 (localVar): " + localVar);

                // 3. 지역 내부 클래스 자신의 멤버 접근
                System.out.println("내부 클래스의 변수 (innerVar): " + innerVar);
                System.out.println("내부 클래스의 this 참조: " + this.innerVar);
            }
        }
        // --- 지역 내부 클래스 선언 끝 ---

        // 지역 내부 클래스의 인스턴스 생성
        System.out.println("LocalInner 인스턴스 생성 직전");
        LocalInner li = new LocalInner();

        // 지역 내부 클래스의 메서드 호출
        li.display();

        System.out.println("outerMethod 실행 완료");
    }
}

public class LocalInnerClass2 {
    public static void main(String[] args) {



    }
}