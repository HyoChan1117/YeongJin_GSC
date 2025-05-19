package learningContents.component.exception;

import java.io.IOException;
import java.security.cert.CertificateException;

// OOP에서 예외를 처리하는 방법
// 1. throws를 사용한 예외 전가 (Checked Exception)
class Foo {
    // 메서드를 호출한 부분에서 예외 처리 구문 작성
    void prt() throws IOException {  // 이 메서드를 호출한 쪽으로 전달하는 키워드
        throw new IOException();
    }
}

// 2. RuntimeException을 직접 던짐 (Unchecked Exception)
class Pos {
    // 메서드를 호출한 부분에서 예외 처리를 하지 않아도 컴파일 오류 없음
    void prt() {
        throw new RuntimeException();
    }
}

public class ExceptionProcess3 {
    public static void main(String[] args) throws Exception {
        throw new Exception();
    }
}
