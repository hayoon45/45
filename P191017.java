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
      ODisk2 d = new ODisk2(8); //depth, dep�� 8
      System.out.println("d width = " + d.width); //width�� 15
      System.out.println("d height = " + d.height + ", area =" + d.area(d)); //height�� 6, area�� super.width*d.height�̹Ƿ� �θ��� width�� �ڽ��� height�� ����. ��, 10*6=60
      d.setdepth(9); //dep, depth = 9
      System.out.println ("d depth = " +d.getdepth()+ ", vol = "+d.vol()); //d.getdepth()�� 9, d.vol()�� 60*9=540
       }
   }
