public class Deadlock {
    static  final Object lock1=new Object();
    static final Object lock2=new Object();
    public static void main(String[] args) {
        Thread t1=new Thread(()->{
            synchronized (lock1){
                System.out.println("THREAD-1:Acquired lock1...");
                try{
                    Thread.sleep(100);
                }catch (Exception e){
                    System.out.println(e.getMessage());
                }
                System.out.println("THREAD-1:Waiting for lock2...");
                synchronized (lock2){
                    System.out.println("THREAD-1:Acquired lock2...");
                }
            }
        });
        Thread t2=new Thread(()->{
            synchronized (lock2){
                System.out.println("THREAD-2:Acquired lock2...");
                try{
                    Thread.sleep(100);
                }catch (Exception e){
                    System.out.println(e.getMessage());
                }
                System.out.println("THREAD-2:Waiting for lock1...");
                synchronized (lock1){
                    System.out.println("THREAD-2:Acquired lock1...");
                }
            }
        });
        t1.start();
        t2.start();
    }
}
