#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
   // dynamically alloc memory 
   const int array_size = argc - 1;
   int *arrptr = NULL;
   arrptr = (int *)malloc(array_size * sizeof(int));
   FILE *output_file;
 
   if (argc < 2) {
       printf("Usage: %s <elements...>\n", argv[0]);
       return 1;
    }

   for (int i = 0; i < array_size; i++) {
       arrptr[i] = atoi(argv[i + 1]);
    }

   output_file = fopen("c_output.txt", "w");
   if (output_file == NULL) {
        printf("Error opening file for writing.\n");
        perror("fopen");
        return 1;
}

    for (int i = 0; i < array_size; i++) {
        printf("%d ", arrptr[i]+1);
        if (arrptr[i] > 170) {
            fprintf(output_file, "%d ", 255);
        } else {
            fprintf(output_file, "%d ", 0);
        }
    }
    fprintf(output_file, "\n");

    fclose(output_file);
   
   free(arrptr);
   arrptr = NULL; 



}
