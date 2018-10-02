#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) {
	int j = 5;
	int *a = &j;
	*a = *a + 4;
	cout << j << endl;
    	return 0;
} 
