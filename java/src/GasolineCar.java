public class GasolineCar extends Car {
    private double tank;
    public GasolineCar(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors, double gasTankSize){
        super(makeAndModel, maximumNumberOfPassengers, numberOfDoors);
        this.tank = gasTankSize;
    }
    public void setGasTankSize(double g){
        this.tank = g;
    }
    public double getGasTankSize(){
        return this.tank;
    }
    public String toString(){
        return super.toString() + "\nGas tank size: " + this.tank;
    }
}