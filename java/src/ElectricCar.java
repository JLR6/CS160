public class ElectricCar extends Car{
    private double bat;
    public ElectricCar(String makeAndModel, int maximumNumberOfPassengers, int numberOfDoors, double batterySize){
        super(makeAndModel, maximumNumberOfPassengers, numberOfDoors);
        this.bat = batterySize;
    }
    public void setBatterySize(double b){
        this.bat = b;
    }
    public double getBatterySize(){
        return this.bat;
    }
    public String toString(){
        return super.toString() + "\nBattery size: " + this.bat;
    }
}