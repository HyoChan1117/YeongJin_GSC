package LearningContents.FlowControl;

public class CodeGroup {
    public static void main(String[] args) {

        int bar = 2;

        // bar 2 이면 참을 출력
        // 컴파일러가 'if()' 가 나오면 조건문 임을 인식
        // () 안에 if문의 조건식이 들어감
        // Java나 C는 기계를 우선적으로 만들어진 언어
        if(bar==2)System.out.println(bar);  // 실행은 가능하지만 가독성이 떨어짐

        // 이렇게 해도 되지만
        if (bar == 2)
            System.out.println(bar);

        // 이렇게 해도 됨 => 유지보수, 가독성(가장 많이 사용되는 방법)
        if (bar == 2) {
            System.out.println(bar);
        }

        // 이렇게 해도 됨
        if (bar == 2)
        {
            System.out.println(bar);
        }

        // Java에서 지역변수는 언제 태어날까? => 변수가 선언될 때
        // 변수가 선언 된 '{}'가 닫힐 때
        {
            int foo = 5;
            System.out.println(foo);
        }

    }
}
