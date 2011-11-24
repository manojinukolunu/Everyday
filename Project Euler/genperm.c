#include <stdio.h>

/*!
    Generates the next try.

    If v is 1 2 1 2, after calls to

        next(v, 4);

    v will be     1 2 1 3

                1 2 1 4

                1 2 2 1

                1 2 2 2

    @return 0, if there are no more valid tries

    @return 1, otherwise
*/
int next(int v[], int n) {
    int i = n - 1;
    v[i] = v[i] + 1;
    while ((i >= 0) && (v[i] > n)) {
        v[i] = 1;
        i--;
        if(i >= 0)
            v[i]++;
    }

    if (i < 0)
        return 0;
    return 1;
}

void printv(int v[], int n) {
    int i;

    for (i = 0; i < n; i++)
        printf("%d ", v[i]);
    printf("\n");
}

/*!
    @return 1, if v is a valid permutation (no digits repeat)

    @return 0, otherwise
*/
int is_perm(int v[], int n) {
    int i, j;

    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (v[i] == v[j])
                return 0;

    return 1;
}

int main(int argc, char *argv[]) {
    int v[128];
    int n = 8;

    /* The initial permutation is 1 2 3 ...*/
    int i;
    for(i = 0; i <= n; i++)
        v[i] = i + 1;

    while (next(v,n))
        if (is_perm(v,n))
            printv(v,n);

    return 0;
}
