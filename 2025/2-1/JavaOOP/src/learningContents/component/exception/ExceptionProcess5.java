package learningContents.component.exception;


import java.io.IOException;

public class ExceptionProcess5 {
    public static void main(String[] args) {

        try {
            int bar = 1;

            if (bar == 1) {
                throw new IOException("IO Exception 발생");
            }
        } catch (Exception e) {
            if (e instanceof IOException) {
                System.out.println(((IOException) e).getMessage());
            }
        }


    }
}
