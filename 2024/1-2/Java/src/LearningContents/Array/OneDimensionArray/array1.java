package LearningContents.Array.OneDimensionArray;

public class array1 {

    static float[] getSumAvg(int a, int b, int c) {
        float result[] = new float[2];

        result[0] = a + b + c;
        result[1] = result[0] / 3;

        return result; // 매서드의 반환 값이 2개 이상일 경우 배열을 이용해서 반환한다.
    }

    public static void main(String[] args) {

        float values[] = getSumAvg(1, 2, 3);
        System.out.println("sum: " + values[0]);
        System.out.println("avg: " + values[1]);

    }
}
