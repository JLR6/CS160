import java.util.ArrayList;

public class FleetOfCars {
    
    private ArrayList<Car> c;
    private int size;
    public FleetOfCars(){
        c = new ArrayList<Car>(); 
        size = 0;
    }
    // public Car search(String s){

    // }
    public void add(Car c1){
        c.add(c1);
        size++;
        System.out.println("Added car");
    }
    public int getSize(){
        return this.size;
    }
    public void delete(int i){
        System.out.println("deleting");
        if (i >= 0 && i < getSize()){
           c.remove(i);
           size --;
        }
        else{
            System.out.println("Please choose a valid index.");
        } 
        
    }
    public Car get(int i){
        return c.get(i);
    }

    public FleetOfCars search(String s){
        FleetOfCars ret = new FleetOfCars();
        for (int i = 0; i < this.size; i++){
            if (s.equals(c.get(i).getMakeAndModel())){
                ret.add(c.get(i));
            }
        }
        return ret;
    }

    public String toString(){
        String ret = "";
        for (int i =0; i<this.size; i++){
            ret += get(i) + " ";
        }
        return ret;
    }
}


