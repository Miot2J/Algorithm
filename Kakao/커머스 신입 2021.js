//자바 코드임
// import java.util.Arrays;
//
// class Solution {
//     public int solution(int[] gift_cards, int[] wants) {
//     int answer = 0;
//     int count = 0;
//     Arrays.sort(gift_cards);
//     Arrays.sort(wants);
//     int index = 0;
//     for (int i : wants) {
//     for (int j=index; j < gift_cards.length;j++) {
//     if(gift_cards[j] > i){
//     break;
// }
// else{
//     if(gift_cards[j] == i){
//
//         count++;
//         index = j+1;
//         break;
//     }
// }
// }
//
// }
// // System.out.print(count);
// answer = gift_cards.length - count;
//
//
// return answer;
// }
// }