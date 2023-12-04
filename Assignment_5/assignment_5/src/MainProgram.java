public class MainProgram{
    public static void main(String[] args) {
        // Queue<Car> q = new Queue<>();
        // q.enqueue(new Car(0, 0, 0));
        // q.enqueue(new Car(1, 0, 0));
        // q.enqueue(new Car(2, 0, 0));
        // System.out.println(q);
        // System.out.println("Now testing dequeuing");
        // q.dequeue();
        // System.out.println(q);
        // System.out.println("Now testing dequeuing");
        // q.dequeue();
        // System.out.println(q);
        // System.out.println("Now testing dequeuing");
        // q.dequeue();
        // System.out.println(q);
        CarRequests cr = new CarRequests();
        cr.addRequests(1);
        cr.addRequests(2);
        cr.addRequests(3);
        cr.addRequests(1);
        cr.addRequests(3);
        cr.addRequests(4);
        cr.printer();
        CarLot cl = new CarLot();
        cl.addCar(new Car(1, 0, 0));
        cl.addCar(new Car(2, 0, 0));
        cl.addCar(new Car(3, 0, 0));
        cl.addCar(new Car(4, 0, 0));
        cl.printer();
        System.out.println("testing process request");
        System.out.println(cl.processRequests(cr));
    }
}