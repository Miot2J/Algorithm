import java.util.Arrays;

public class k번째수 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
//        int index = 0;

        for (int i = 0; i < commands.length; ++i) {
//            new int[ints[1] - ints[0] +1];1
            int[] newArray = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);


            Arrays.sort(newArray);
            answer[i] = newArray[commands[i][2]-1];
//            index++;
        }

        return answer;
    }
}
