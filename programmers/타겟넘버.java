public class 타겟넘버 {
        public int solution(int[] numbers, int target) {
            int answer = 0;
            int value = 0;
            int numbersSize = numbers.length;
            answer = makeAnswer(numbers,0,target,value);
            return answer;
        }

        private int makeAnswer(int[] numbers, int index, int target,int value){
            int answer = 0;
            if(index == numbers.length -1){
                value += numbers[index];
                if(value == target){
                    return 1;
                }
                value -= numbers[index] *2;
                if(value == target){
                    return 1;
                }
                if(value != target){
                    return 0;
                }
            }
            else{
                value += numbers[index];
                answer += makeAnswer(numbers,index+1,target,value);
                value -= numbers[index] *2;
                answer += makeAnswer(numbers,index+1,target,value);
            }

            return answer;
        }
}
