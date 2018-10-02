#include <stdio.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen("/home/carlos/Documents/CodeEval/TestFiles/PenultWord", "r");
    char line[1];
    while (fgets(line, 1, file)) {
        printf("%s",line);
    }
    return 0;
} 
