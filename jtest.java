
class JTest {
    private int x =0;
    private String peter ="peter";

    public JTest()
    {
        System.out.println(this.x);
        System.out.println(this.peter);
    }
    
    public static void main(String[] args) {
        JTest test =new JTest();    
    }
}