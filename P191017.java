class ODisk {
   public int width=5;
   public ODisk(){}
   }

class ODisk1 extends ODisk {
   protected int height=6, width=10;
   public ODisk1(){}
   public int area(ODisk2 d) {
      return super.width * d.height;}
   }

class ODisk2 extends ODisk1 {
    private int depth=7;
public int width=15;
    public ODisk2(int dep){
       depth = dep;}
    public int getdepth() {
return depth;}
    public void setdepth(int dep) {
      depth = dep;}
    public int vol() {
       return area(this)* depth; }
   }

public class P191017 {
   public static void main(String argv[]) {
      ODisk2 d = new ODisk2(8); //depth, dep은 8
      System.out.println("d width = " + d.width); //width는 15
      System.out.println("d height = " + d.height + ", area =" + d.area(d)); //height는 6, area는 super.width*d.height이므로 부모의 width와 자식의 height의 곱임. 즉, 10*6=60
      d.setdepth(9); //dep, depth = 9
      System.out.println ("d depth = " +d.getdepth()+ ", vol = "+d.vol()); //d.getdepth()는 9, d.vol()은 60*9=540
       }
   }
