#include <iostream>
using namespace std;

int main() {

  int vetor[10]; // declaração de vetor
  vetor[0] = 50;

  for (int i = 0; i<10; i++) {
    vetor[i] = i + 100;
  }

  cout << vetor[1] << endl; 

      
  return 0;
}