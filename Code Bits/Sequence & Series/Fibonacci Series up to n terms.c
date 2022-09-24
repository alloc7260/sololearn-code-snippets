#include <stdio.h>
int main()
{ 
 int i, n, t1 = 0, t2 = 1;
 int nextTerm = 0;
 printf("Enter the number of terms: ");
 scanf("%d", &n);
 printf("\nFibonacci Series: ");
 for (i = 1; i <= n; ++i)
 { 
  printf("\n%d", nextTerm);
  t1 = t2;
  t2 = nextTerm;
  nextTerm = t1 + t2;
 }
return 0;
}