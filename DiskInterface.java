class Disk {
	public int width=5;
	public Disk(){}
	}
class Disk1 extends Disk {
	protected int height=6;
	public Disk1(){}
	}
interface DiskAreaVol {
	int area();
	int vol(); //
	}
interface NoDisk extends DiskAreaVol {
	int count=0;
	int communication();
	}
abstract class Disk2 extends Disk1 implements NoDisk {
	public int depth=7;
	public Disk2(){}
	abstract public int area();
	abstract public int vol();
	}
class Disk3 extends Disk2 {
	int count = 1;
	public Disk3() {}
	public Disk3(int d) {this.width=d;}
	public int communication() {
		int total = area()+vol();
		return total;
	}
	public int area() {
		return this.width*this.height;
	}
	public int vol() {
		return area()*this.depth;
	}
}

public abstract class DiskInterface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Disk3 d = new Disk3(4);
		System.out.println("area = "+d.area());
		System.out.println("vol = "+d.vol());
		System.out.println("noDisk = "+d.communication());
		System.out.println("count = "+d.count);
	}

}
