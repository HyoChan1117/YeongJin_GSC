package LearningContents.FlowControl;

public class CodeGroup1 {
    public static void main(String[] args) {

        // bar 2 이면 참을 출력
        // 컴파일러가 'if()' 가 나오면 조건문 임을 인식
        // () 안에 if문의 조건식이 들어감
        // Java나 C는 기계를 우선적으로 만들어진 언어 => 들여쓰기는 의미가 없음
        // 코드를 그룹화 하는 방법 => ;
        // '{}'를 이용해서 코드를 그룹화 함  => 파이썬에서는 들여쓰기로 그룹화
        // code group or block

        int bar = 3;
        if (bar == 2) {
            System.out.println("bar");  // ';'은 컴파일러가 코드를 구분하기 위해 사용
            System.out.println("foo");  //
        }
    }
}
