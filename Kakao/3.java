public int solution(int[] A) {
      int result = 0;
      if(A.length == 1)
         return 1;
      if(A.length == 2)
         return 2;
      int[][] dp = new int [A.length][A.length];
      int even = 0;
      int odd = 0;
      for(int i = 2; i < A.length; i++) {
         dp[i-2][i-2] = 1;
         dp[i-2][i-1] = 2;
         even = A[i-2];
         odd = A[i-1];
         for(int j = i; j < A.length; j++) {
            if(((j - i) % 2 == 0 && A[j] != even) || ((j - i) % 2 != 0 && A[j] != odd)){
               break;
            }
            else {
               dp[i-2][j] = dp[i-2][j-1] + 1;
            }
         }
         for (int k : dp[i-2]) {
            result = Math.max(k, result);
         }
      }
      return result;
   }