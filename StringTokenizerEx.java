import java.util.StringTokenizer;

public class StringTokenizerEx {
    public static void main(String[] args) {
       String query = "name=aaa&addr=seoul&age=21#name=bbb&addr=Busan#name=ccc&addr=Daejun&age=26";
       StringTokenizer st = new StringTokenizer(query, "#");
       
       String array[][];
       array = new String[3][3];
       int i=0;
      
       while(st.hasMoreTokens()) {
    	   String token = st.nextToken();
    	   StringTokenizer str = new StringTokenizer(token, "&");
    	   int j=0;
    	   while(str.hasMoreTokens()) {
    		   String tokens = str.nextToken();
    		   array[i][j]=tokens;
    		   j = j+1;
    	   }
    	   i=i+1;
       }
       
       for(i=0;i<3;i++) {
    	   for(int j=0;j<3;j++) {
    		   String word = array[i][j];
    		   if(word!=null) {
    			   String[] array2 = word.split("=");
	    		   System.out.printf("%s\t", array2[1]);
    		   }
    		   else System.out.printf(" \t");
    	   }
    	   System.out.println("\n");
       }   
    }
}