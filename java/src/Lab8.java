class Lab8 {
    public static void main(String[] args){
            System.out.println(checkReply("Hello", 'h'));
            System.out.println(checkReply("hello", 'h'));
            System.out.println(checkReply("yes", 'h'));
            System.out.println(checkReply("Yes", 'h'));
            System.out.println(checkReply("123", 'h'));
            System.out.println(checkReply("", 'h'));
    }

    public static boolean checkReply(String s, char c){
        if(s.length()==0){
            return false;
        }
        char comp = s.toLowerCase().charAt(0);
        if(comp == c){
            return true;
        }
        else{
            return false;
        }
    }
}
