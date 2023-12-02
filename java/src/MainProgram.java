import java.util.Scanner;
public class MainProgram {
    public static void main(String[] args) throws Exception {
        // tester();
        FleetOfCars f = new FleetOfCars();
        boolean running = true;
        Scanner obj = new Scanner(System.in);
        while (running){
            System.out.println("Enter option from list below: \n1) Display complete directory \n2) Enter new car \n3) Search for car \n4) Modify car information \n5) Delete a record \n6) Quit \nEnter your option:");
            String in = obj.nextLine();
            in = in.toLowerCase().substring(0,1);
            if(isNumeric(in)){
                if(in.equals("6")){
                    running = false;
                }
                else if (in.equals("5")){
                    if (f.getSize()>0){
                        System.out.println("Which object would you like to delete?");
                    int choice = 0;
                    int reloop = 0;
                    do {
                        try {
                            String input = obj.nextLine(); // Scan the next line from System.in
                            choice = Integer.parseInt(input); // Try to parse it as an int
                            reloop++;
                        } catch (Exception e) {
                            System.out.println("Please enter a number!");
                        }
                    } while (reloop == 0);
                    f.delete(choice);
                    }
                    else{
                        System.out.println("Nothing to delete");
                    }   
                }
                else if (in.equals("4")){
                    if (f.getSize()>0){
                        System.out.println("Enter the make and model of the car you would like to modify: ");
                        String inn = obj.nextLine();
                        System.out.println("Please choose which car to modify:");
                        int lister =0;
                        FleetOfCars ff = f.search(inn);
                        Car modCar = new Car("none", 0, 0);
                        if (ff.getSize()>0){
                            for (int s =0; s<ff.getSize(); s++){
                                System.out.print(ff.get(lister));
                                System.out.println("\nWould you like to modify this car? (Y/N)");
                                String ch = obj.nextLine();
                                ch = ch.toLowerCase().substring(0, 1);
                                if (ch.equals("y")){
                                    modCar = ff.get(lister);
                                    System.out.println("What would you like to modify? \n1) Make and model \n2) Max passengers \n3) Number of doors");
                                    int inp= 0;
                                    int looper = 0;
                                    do {
                                        try {
                                            String input = obj.nextLine(); // Scan the next line from System.in
                                            inp = Integer.parseInt(input); // Try to parse it as an int
                                            looper++;
                                        } catch (Exception e) {
                                            System.out.println("Please enter a number!");
                                        }
                                    } while (looper == 0);
                                    
                                    if (inp == 1){
                                        
                                        System.out.println("Please type the new make and model: ");
                                        String st = obj.nextLine();
                                        modCar.setMakeAndModel(st);
                                        System.out.println("Modified.");
                                    }
                                    else if (inp == 2){
                                        System.out.println("Please type the new max passengers: ");
                                        int inpu = obj.nextInt();
                                        modCar.setMaximumNumberOfPassengers(inpu);
                                        System.out.println("Modified.");
                                    }
                                    else if (inp == 3){
                                        System.out.println("Please type the new number of doors: ");
                                        int inpu = obj.nextInt();
                                        modCar.setNumberOfDoors(inpu);
                                        System.out.println("Modified.");
                                    }
                                    else{
                                        System.out.println("Please choose a valid option.");
                                    }    
                                }
                                else{
                                    lister++;
                                }
                            }
                        }
                    }
                    else{
                        System.out.println("Nothing to modify");
                    } 
                }
                else if (in.equals("3")){
                    if(f.getSize()>0){
                        System.out.println("Please type the index of the car you want to search for: ");
                        int b = 0;
                        int reloop =0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                b = Integer.parseInt(input); // Try to parse it as an int
                                reloop++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (reloop == 0);
                        
                        if (b >=0&& b<f.getSize()){
                            System.out.println(f.get(b));
                        }
                        else{
                            System.out.println("Please input a valid index");
                        }
                    }
                    else{
                        System.out.println("Nothing to search for");
                    }
                    
                }
                else if (in.equals("2")){
                    System.out.println("Please choose what kind of car to add: \n1) Car \n2) Electric car \n3) Gasoline car");
                    int i = 0;
                    int rev=0;
                    do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                i = Integer.parseInt(input); // Try to parse it as an int
                                rev++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (rev == 0);
                    if (i == 1){
                        System.out.println("Please input the make and model: ");
                        String a = obj.next();
                        obj.nextLine();
                        
                        System.out.println("Please input the max number of passengers: ");
                        int b = 0;
                        int reloop = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                b = Integer.parseInt(input); // Try to parse it as an int
                                reloop++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (reloop == 0);
                        System.out.println("Please input the number of doors: ");
                        int c = 0;
                        int re = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                c = Integer.parseInt(input); // Try to parse it as an int
                                re++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (re == 0);
                        Car c1 = new Car(a, b, c);
                        f.add(c1);
                    }
                    else if (i == 2){
                        System.out.println("Please input the make and model: ");
                        String a = obj.next();
                        obj.nextLine();
                        
                        System.out.println("Please input the max number of passengers: ");
                        int b = 0;
                        int reloop = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                b = Integer.parseInt(input); // Try to parse it as an int
                                reloop++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (reloop == 0);
                        System.out.println("Please input the number of doors: ");
                        int c = 0;
                        int re = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                c = Integer.parseInt(input); // Try to parse it as an int
                                re++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (re == 0);
                        System.out.println("Please input the battery size: ");
                        double d = 0;
                        int r = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                d = Double.parseDouble(input); // Try to parse it as an int
                                r++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (r == 0);
                        ElectricCar e1 = new ElectricCar(a, b, c, d);
                        f.add(e1);
                    }
                    else if (i==3){
                       System.out.println("Please input the make and model: ");
                        String a = obj.next();
                        obj.nextLine();
                        
                        System.out.println("Please input the max number of passengers: ");
                        int b = 0;
                        int reloop = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                b = Integer.parseInt(input); // Try to parse it as an int
                                reloop++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (reloop == 0);
                        System.out.println("Please input the number of doors: ");
                        int c = 0;
                        int re = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                c = Integer.parseInt(input); // Try to parse it as an int
                                re++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (re == 0);
                        System.out.println("Please input the tank size: ");
                        double d = 0;
                        int r = 0;
                        do {
                            try {
                                String input = obj.nextLine(); // Scan the next line from System.in
                                d = Double.parseDouble(input); // Try to parse it as an int
                                r++;
                            } catch (Exception e) {
                                System.out.println("Please enter a number!");
                            }
                        } while (r == 0);
                        
                    
                        GasolineCar g1 = new GasolineCar(a, b, c, d);
                        f.add(g1);
                    }
                    else{
                        System.out.println("Please choose a valid option.");
                    }
                }
                else if (in.equals("1")){
                    System.out.println(f);
                }
                else{
                    System.out.println("Please enter a valid input.");
                }
            }
            else{
                System.out.println("Please enter a valid input.");
            }

        }
        obj.close();
    }
    public static boolean isNumeric(String str) { 
        try {  
          Double.parseDouble(str);  
          return true;
        } catch(NumberFormatException e){  
          return false;  
        }  
      }

    public static void tester(){
        FleetOfCars fleet = new FleetOfCars();
        fleet.add(new Car("dodge", 5, 4));
        fleet.add(new ElectricCar("electric dodge", 0, 0, 6));
        fleet.add(new GasolineCar("gas dodge", 5,4,7.0));
        System.out.println(fleet);
        fleet.delete(1);
        System.out.println(fleet);


    }
}