#include <stdio.h>

int grid_numbers [9][9];

void intialise(){
    for(int row = 0; row < 9;){
        int column = 0;
            
            for(; column < 9; column++){
                grid_numbers[row][column] = 0;
            }
        
        row = row+1;
    }  
}

void printing(){
    for(int row = 0; row < 9;){
        int column = 0;
            
            for(; column < 9; column++){
                grid_numbers[row][column] = 0;
                printf("%d ", grid_numbers[row][column]);
            }

        printf("\n");
        
        row = row+1;
        
    }  
}

int main() {
    intialise();
    printing();
    return 0;
}
