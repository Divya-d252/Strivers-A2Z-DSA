//User function Template for Java
class Solution{
    static String compareNM(int n,int m){
        // code here
        String s= "";
        if(n<m){
            s="lesser";
        }
        else if(n>m){
            s="greater";
        }
        else{
            s = "equal";
        }
        return s;
    }
}
