import java.util.Arrays;
import java.util.Comparator;

/*
        여행경로 solution = new 여행경로();
//        String[][] tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}};
//        String[][] tickets = {{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}};
                String[][] tickets ={{ "ICN", "BOO" }, { "ICN", "COO" }, { "COO", "DOO" }, { "DOO", "COO" }, { "BOO", "DOO" },{ "DOO", "BOO" }, { "BOO", "ICN" }, { "COO", "BOO" }};
                String[][] tickets1 = {{"ICN","A"},{"A","B"},{"A","C"},{"C","A"},{"B","D"}};
                System.out.println(solution.solution(tickets1));
                System.out.println();

*/

public class 여행경로 {

        public String[] solution(String[][] tickets) {
            String[] answer = new String[tickets.length+1];
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

            if(index == answer.length-1 ){
                answer[index] = airport;
                return answer;
            }

            for(int i = 0; i < tickets.length; i++){
                if(tickets[i][0].equals(airport)){
                    answer[index] = tickets[i][0];

                    for(int j = 0; j < tickets.length; j++){

                        if(tickets[i][1].equals( tickets[j][0]) ){
                            tickets[i][0] = "USE";
                            BFS(tickets,tickets[i][1],answer,index+1);

                        }
                        if(index == answer.length-2 ){
                            BFS(tickets,tickets[i][1],answer,index+1);
                        }
                    }
                }
            }
            for(String s : answer){
                System.out.println(s);
            }
            System.out.println();
            return answer;
        }

    }