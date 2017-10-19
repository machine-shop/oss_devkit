/*
Given a list,
Display it in vertical order, ensuring that all rows are full (except possibly the last one.)


a b c d e f g

Wrong:
a b c
d e f
g

Wrong:
a d g
b e
c f

Correct:
a d f
b e g
c


*/


public void printInOrder(char[] arr, int x){
    int length = arr.length;
    int remainder = length%x;
    int rows = length/x;
    int count = 0;
    for(int i = 0; i<rows; i++){
        int currIndex = i;
        for(int y = 0; y<x; y++){
            int toAdd = rows;
            if(count < remainder){
                toAdd++;
            }
            System.out.print(arr[toAdd]);
        }
    }
}
