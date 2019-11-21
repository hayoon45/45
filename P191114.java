import java.util.Vector;
import java.util.Scanner;

class MyVec1<T>{
	Vector<T> vec = new Vector<T>( );
	   public void addE(T item) {
	      vec.add(item);
	   }
	   public T removeFirstE() {      
	      return vec.remove(0);
	   }
	   public T removeLastE() {     
	      return vec.remove(vec.size()-1);
	   }
	   public int noE() {
		  return vec.size();
	   }
	}

public class P191114 {
	public static void main(String[] args) {
		MyVec1<String> MV = new MyVec1<String>();
	    Scanner scanner = new Scanner(System.in);
	    
	    System.out.print("도시를 입력하고 끝내려면 x를 입력하세요~ \n");
	    for(;;) {
	    	String city = scanner.next();
	    	if(city.equals("x")) {
	    		break;
	    	}
	    	MV.addE(city);
	    }
	    
	    System.out.print("Stack은 S, Queue는 Q를 입력하세요~ \n");
	    String input = scanner.next();
	    int noE = MV.noE();
	    for(int j=0;j<noE;j++) {
	        if(input.contentEquals("S")) {
	        	System.out.println(MV.removeLastE());
	        }
	        if(input.contentEquals("Q")) {
	           System.out.println(MV.removeFirstE());
	        }
	    }
	    scanner.close();
	}
}