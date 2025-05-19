package learningContents.component.exception;

import java.io.IOException;
import java.security.cert.CertificateException;

public class ExceptionProcess {
    public static void main(String[] args) {  // Exception 예외 던지기

        int pos = 0;

        // try-catch or throws
        // try : 해피 시나리오
        try {
            // throw : 예외 객체를 직접 발생시키는 역할
            // throw 뒤에는 Throwable의 자식 클래스들만 올 수 있음
            System.out.println("t-1");

            // try문 내에서 예외가 1개라도 발생하면 다음 코드는 실행하지 않음
            // 예외 발생 시 예외 발생한 시점부터 해피 시나리오는 끝!
            // 바로 catch 구문으로 넘어감
            if(pos == 0)
                throw new Exception();  // 예외 발생!!
            if (pos == 1)
                throw new CertificateException();
            if (pos == 2)
                throw new IOException();

            // 위에서 예외가 발생 했을 경우 실행되지 않음
            // 위에서 예외가 발생하지 않았을 경우 실행됨 (Python Exception에서의 else와 동일)
            System.out.println("t-2");
        }

        // catch : 예외 처리 구문
        // catch 문의 개수 try 문에서 발생할 수 있는 예외의 종류
        // 다형성 제공 : 매개변수 클래스의 상속 관계도를 확인해야 함
        // -> 자식 클래스형 보다 부모 클래스형이 먼저 오게 하면 안됨
        // -> 무조건 자식 클래스형이 위 쪽에 올 수 있게 해야 함
        // 다양한 예외 종류를 처리할 때는 Exception은 가장 밑에 하기
        catch (CertificateException e) {
            System.out.println("CertificateException");
        }
        catch (IOException e) {
            System.out.println("IOException");
        }
        catch (Exception e) {
            System.out.println("Exception");
        }

        // 예외 처리가 끝난 후 순차적으로 실행
        System.out.println("t-3");
    }
}
