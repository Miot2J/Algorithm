import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;

public class 여행경로 {

        public String[] solution(String[][] tickets) {
            String[] answer = new String[tickets.length];
            Arrays.sort(tickets, new Comparator<String[]>() {
                @Override
                public int compare(final String[] entry1, final String[] entry2) {
                    final String depart1 = entry1[1];
                    final String depart2 = entry2[1];
                    return depart1.compareTo(depart2);
                }
            });

            return BFS(tickets,"ICN",answer,0);
        }
        private String[] BFS(String[][] tickets, String airport,String[] answer,int index){

            if(answer[answer.length-1] != null){
                return null;
            }
            for(String[] ticket : tickets){
                if(ticket[0].equals(airport)){
                    answer[index] = ticket[0];
                    BFS(tickets,ticket[1],answer,index+1);
                }
            }
            return answer;
        }

    }
