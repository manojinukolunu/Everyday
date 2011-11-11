#include <stdio.h>

int generateTriangle(int i){
  return i*(i+1)/2;
}
int divisors(int n){
  int limit=n;
  int count=0;
  int i;
  for(i=1;i<limit;++i){
    if (n%i==0){
      limit=(int)n/i;
      count++;
    }
  }
  return count*2;
}
int main(int argc,char **argv){
 long i=100;
  while (1){
    long n=generateTriangle(i);
    int count=divisors(n);
    if (count>500){
      printf("%ld\n",n);
      break;
    }
    i++;
  }
  return 0;
}
