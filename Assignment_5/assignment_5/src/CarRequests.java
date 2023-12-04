public class CarRequests {
    private Queue<Integer> q;
    public CarRequests(){
        q = new Queue<>();
        
    }
    public void addRequests(int x){
        q.enqueue(x);
     
    }
    public int getRequest(){
        return q.dequeue();
    }
    public boolean hasPendingRequests(){
        if(q.isEmpty()){
            return false;
        }
        else{
            return true;
        }
    }
    public void printer(){
        System.out.println(q);
    }
}
