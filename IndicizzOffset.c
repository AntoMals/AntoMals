#include<stdio.h>
#define ARRAY_SIZE 4

int main (void){
    int b[]={10,20,30,40};//crea e inizializza l'array b
    int *bPtr=b; //crea bPtr e fallo puntare all'array b

    /*stampa l'array b usando la notazione degli array con indice*/
    puts("Array b printed with:\nArray subscript notation");

    /*effetua un ciclo lungo l'array b */
    for (size_t i=0; i < ARRAY_SIZE;++i){
        printf("b[%zu]=%d\n", i, b[i]);
    }
    //stampa l'array b con il nome e la notazione puntatore/offset
    puts("\nPointer/offset notation where the pointer is the array name");

    //effettua un ciclo lungo l'array b
    for (size_t offset=0; offset < ARRAY_SIZE; ++offset){
        printf("*(b + %zu) = %d\n", offset, *(b + offset));
    }
    /*stampa l'array b con bPtr e la notazione degli array con indice*/ 
    puts("\nPointer subscription notation");
    //effettua un ciclo lungo l'array b
    for (size_t i =0; i <ARRAY_SIZE; ++i){
        printf("bPTR[%zu]=%d\n", i, bPtr[i]);

    }
    //stampa l'array b usando bPTR e la notazione puntatore/offset
    puts("\nPointer/offset notation");
    
    //effettua un ciclo lungo l'array b
    for (size_t offset=0; offset < ARRAY_SIZE; ++offset) {
        printf("*(bPTR + %zu) = %d\n", offset, *(bPtr + offset));
    }
}
