#include <stdio.h>
#include <stdbool.h>

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

void printing_0(){
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

void printing_8(){
    for(int row = 0; row < 9;){
        int column = 0;
            
            for(; column < 9; column++){
                grid_numbers[row][column] = 8;
                printf("%d ", grid_numbers[row][column]);
            }

        printf("\n");
        
        row = row+1;
        
    }  
}

void check_if_filled(){
    bool grid_filled_verifier = true;
    
    for(int row = 0; row < 9;){
        int column = 0;
        
        for(; column < 9;){
            
            if (grid_numbers[row][column] == 0){
               grid_filled_verifier = false;
            }

        column = column + 1;
        }
    row = row + 1;
            
    }
    
    if (grid_filled_verifier == false){
        printf("Sudoku Grid has not been successfully filled! \n");
    }
    
    else{
        printf("Sudoku Grid has been successfully filled! \n");
    }
    
}

int main() {
    intialise();
    printing_0();
    check_if_filled();
    printing_8();
    check_if_filled();
    return 0;
}
