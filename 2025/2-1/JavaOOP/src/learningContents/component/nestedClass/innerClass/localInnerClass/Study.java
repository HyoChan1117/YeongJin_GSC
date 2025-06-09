package learningContents.component.nestedClass.innerClass.localInnerClass;

class InnerClass {
    // Inner class의 Member class
    class InnerInnerClass {}

    // 메서드 내 클래스 선언
    void prt() {
        class LocalInner {}
    }
    
    // 초기화 블록 내 클래스 선언
    {
        class LocalInner1 {}
    }
    
    // 생성자 내 클래스 선언
    InnerClass() {
        class LocalInner2 {}
    }
}

public class Study {
    public static void main(String[] args) {
        
        
        
    }
}
