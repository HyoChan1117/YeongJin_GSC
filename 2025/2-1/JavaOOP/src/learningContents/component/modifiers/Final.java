package learningContents.component.modifiers;

// 클래스 앞 final -> 상속 못함
final class Bar {
    // 변수 앞 final -> 상수 : 값을 변경 못함
    // 상수 값의 초기화 방법
    // 1. 선언과 동시에!
    final int bar = 1;
    final int pos;
    final int kin;
    // 2. 생성자에서 초기화
    Bar () {
        pos = 2;
    }
    // 3. 초기화 블록에서 초기화
    {
        kin = 3;
    }

    // 메서드 앞 final -> 오버라이딩 못함
    final void prt(){
        System.out.println("Bar");
    }
}

public class Final {

}
