public class Car {
    private String mm;
    private int max;
    private int doors;
    public Car(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors){
        this.mm = makeAndModel;
        this.max = maximumNumberOfPassengers;
        this.doors = numberOfDoors;
    }
    public void setMakeAndModel(String m){
        this.mm = m;
    }
    public String getMakeAndModel(){
        return this.mm;
    }
    public void setMaximumNumberOfPassengers(int m){
        this.max = m;
    }
    public int getMaximumNumberOfPassengers(){
        return this.max;
    }
    public void setNumberOfDoors(int m){
        this.doors = m;
    }
    public int getNumberOfDoors(){
        return this.doors;
    }
    public String toString(){
        return "Make and model: " + this.mm + "\nMax number of passengers: " + this.max + "\nNumber of doors: " + this.doors;
    }
}