#include<stdio.h>
#include "7.h"

int str_end( char *s, char *t)
{
    const char *init = t;       /* Hold the initial position of *t */

    while (*s) {
        while (*s == *t) { 
            if (!(*s)) {
                return 1;
            }
            s++;
            t++;
        }
        s++;
        t = init;
    }
    return 0;
}