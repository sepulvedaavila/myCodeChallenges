#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <sstream>

using namespace std;
string busca(string pal);

int main(int argc, char *argv[]) {
	ifstream stream(argv[1]);
	string line;
	while(getline(stream, line)) {
		string num;
		stringstream stream(line);
		while(getline(stream, num, ',') ){
			busca(num);
		}
	}
		return 0;
	}

	string busca(string num){
		for(int x=0;x<num.size();x++){
			if(num[x]==';'){
			for(int y=x+1;y<num.size();y++){
				cout<<num[y];
			}
		cout<<endl;
		}
	}
}

