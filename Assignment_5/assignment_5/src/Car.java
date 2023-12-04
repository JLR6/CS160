public class Car{
    private int id;
    private int powerSource;
    private float pricePerDay;
    public Car(int i, int p, int ppd){
        this.id =i;
        this.powerSource = p;
        this.pricePerDay = ppd;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        if(id>0 && id<4){
            this.id = id;
        }
        
    }

    public int getPowerSource() {
        return this.powerSource;
    }

    public void setPowerSource(int powerSource) {
        this.powerSource = powerSource;
    }

    public float getPricePerDay() {
        return this.pricePerDay;
    }

    public void setPricePerDay(double pricePerDay) {
        this.pricePerDay = (float)pricePerDay;
    }
    public String toString(){
        return "Id: " + this.id; 
    }

}