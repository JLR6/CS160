import java.util.ArrayList;
public class Queue<T>{
    private ArrayList<T> list;
    private int front;
    private int back;
    public Queue(){
        list = new ArrayList<>();
        front = -1;
        back = -1;
    }
    public void enqueue(T e){
        list.add(e);
    }
    public T dequeue(){
        if(this.isEmpty()){
            throw new RuntimeException("Queue empty");
        }
        else if (front == back){
            T ret = list.get(front);
            front =-1;
            back = -1;
            return ret;
        }
        else{
            T ret = list.get(front);
            front--;
            return ret;

        }
    }
    public T peek(){
        if(this.isEmpty()){
            throw new RuntimeException("Queue is empty");
        }
        else{
            T ret = list.get(front);
            return ret;
        }
    }
    public boolean isEmpty(){
        if(front ==-1 && back ==-1){
            return true;
        }
        return false;
    }


}  