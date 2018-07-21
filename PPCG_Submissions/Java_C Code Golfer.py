def Java_and_C_Code_Golfer(n):
    import re;
    b=n.split('\n')
    c=re.split('(?<=\{|;|\})\s+',''.join(b))
    print(''.join(c))
    print(len(''.join(c)))

Java_and_C_Code_Golfer('''import java.util.*;import org.openqa.selenium.*;import org.openqa.selenium.firefox.*;
class A{
	interface P{WebElement I(String L);}
	static void Y(String U,String P){
		WebDriver D=new FirefoxDriver();
		P O=L->D.findElement(By.name(L));
		D.get("http://www.codegolf.stackexchange.com/users/login");
		O.I("email").sendKeys(U);
		WebElement Z=O.I("password");
		Z.sendKeys(P);
		Z.submit();
		D.get("http://www.codegolf.stackexchange.com/questions/84546");
		D.findElement(By.linkText("add a comment")).click();
		WebElement V=O.I("comment");
		V.sendKeys("1234567890123456");
		D.findElement(By.xpath("//input[@value='Add Comment']")).click();
	}
	public static void main(String[]a){
		Scanner I=new Scanner(System.in);
		Y(I.next(),I.next());
	}
}''')

Java_and_C_Code_Golfer('''import java.util.*;import org.openqa.selenium.*;import org.openqa.selenium.firefox.*;
class A{
	static void Y(String U,String P){
		WebDriver D=new FirefoxDriver();
		D.get("http://www.codegolf.stackexchange.com/users/login");
		D.findElement(By.name("email")).sendKeys(U);
		WebElement Z=D.findElement(By.name("password"));
		Z.sendKeys(P);
		Z.submit();
		D.get("http://www.codegolf.stackexchange.com/questions/84546");
		D.findElement(By.linkText("add a comment")).click();
		WebElement V=D.findElement(By.name("comment"));
		V.sendKeys("1234567890123456");
		D.findElement(By.xpath("//input[@value='Add Comment']")).click();
	}
	public static void main(String[]a){
		Scanner I=new Scanner(System.in);
		Y(I.next(),I.next());
	}
}''')

Java_and_C_Code_Golfer('''class A{
	interface P{int U(int a);}
	public static void main(String[]a){
		P I=S->Integer.parseInt((Integer.toString(S)+Integer.toString(S)))*S;
		System.out.print(I.U(Integer.parseInt(a[0])));
	}
}''')

Java_and_C_Code_Golfer('''import java.awt.*;
import javax.swing.*;
class A extends JPanel{
	public void paintComponent(Graphics G){
		super.paintComponent(G);
		G.setColor(new Color(0,72,224));
		G.fillRect(0,0,175,126);
		G.setColor(Color.WHITE);
		G.fillRect(49,0,28,126);
		G.fillRect(0,49,175,28);
		G.setColor(new Color(215,40,40));
		G.fillRect(56,0,14,126);
		G.fillRect(0,56,175,14);
	}
	public static void main(String[]a){
		JFrame J=new JFrame();
		J.add(new A());
		J.setSize(175,147);
		J.setVisible(true);
	}
}''')

# Java_and_C_Code_Golfer('''class Flag_of_Ireland{
#     public static void main(String[]a){
#         String V="\u001B[0m";
#         String R="\u001B[31m";
#         String W="\u001B[37m";
#         String B="\u001B[34m";
#         String T=B;
#         String X="";
#         for(int i=0;i<7;i++){T+="0";}
#         T+=W+"0"+R;
#         for(int d=0;d<2;d++){T+="0";}
#         T+=W+"0"+B;
#         for(int y=0;y<14;y++){T+="0";}
#         for(int g=0;g<7;g++){X+="\n"+T;}
#         String A="\n"+W;
#         for(int Z=0;Z<8;Z++){A+="0";}
#         A+=R;
#         for(int S=0;S<2;S++){A+="0";}
#         A+=W;
#         for(int F=0;F<15;F++){A+="0";}
#         String D="\n"+R;
#         for(int v=0;v<25;v++){D+="0";}
#         X+=A+D+D+A+X;
#         System.out.println(X+V);
#     }
# }''')

Java_and_C_Code_Golfer(r'''uint64_t F(int x){return x<1 ? 0:x==1 ? 1:F(x-1)+F(x-2);}
uint64_t G(int H){uint64_t P=1;for(int B=3;B<=H;B++)P*=F(B);return P;}
main(int argc,char**argv){
  int U=atoi(argv[1]);
  int Y=atoi(argv[2]);
  printf("%llu\n",G(U)/(G(U-Y)*G(Y)));
}''')

Java_and_C_Code_Golfer('''class Terminal_Bouncing_Ball{
    static throws InterruptedException{
        int X=0,Y=0,x=1,y=1;
        for(;;){
            System.out.print(String.format("\033[%d;%dH",X,Y));
            Thread.sleep(50);
            x=X<1?1:X>71?-1:x;
            y=Y<1?1:Y>237?-1:y;
            X+=x;
            Y+=y;
        }
    }
}''')
