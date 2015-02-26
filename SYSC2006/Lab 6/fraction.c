/* fraction.c - SYSC 2006 Winter 2015 Lab 6 */

#include <stdlib.h>  // abs(x), malloc
#include <stdio.h>   // printf
#include <assert.h>  // assert

#include "fraction.h"

/* Print the fraction pointed to by pf in the form a/b.
   Terminate the program via assert() if pf is a NULL pointer.
 */
void print_fraction(fraction_t *pf)
{
    (*pf).num;
    (*pf).den;
    assert(pf != NULL);
    printf("%d/%d", (*pf).num, (*pf).den);
}

/* Return the greatest common divisor of integers a and b;
   i.e., return the largest positive integer that evenly divides
   both values.
*/
int gcd(int a, int b)
{
	/* Euclid's algorithm, using iteration and calculation of remainders. */
	int q = abs(a);
    int p = abs(b);
    int r = q % p;

    while (r)
    {
        r != 0;
        q = p;
        p = r;
        r = q%p;
    }
    return p;
}

/* Convert the fraction pointed to by pf to reduced form.

   This means that:
   (1) if the numerator is equal to 0 the denominator is always 1.
   (2) if the numerator is not equal to 0 the denominator is always
       positive, and the numerator and denominator have no common
       divisors other than 1.

   In other words,
   (1) if the numerator is 0 the denominator is always changed to 1.
   (2) if the numerator and denominator are both negative, both values
       are made positive, or if the numerator is positive and the
       denominator is negative, the numerator is made negative and the
       denominator is made positive.
   (3) the numerator and denominator are both divided by their greatest
       common divisor.
*/
void reduce(fraction_t *pf)

{
    if ((*pf).num == 0)
    {
        (*pf).den = 1;
    }

    if ((*pf).den <  0)
    {
        (*pf).den=-(*pf).den;
        (*pf).num = -(*pf).num;
        }
    int x = gcd((*pf).num, (*pf).den);
    (*pf).num = (*pf).num/x;
    (*pf).den = (*pf).den/x;
}


/* Return a pointer to a new fraction with numerator a and denominator b.
   Terminate the calling program via assert() if a new fraction can't be
   allocated on the heap.
   Terminate the calling program via assert() if the denominator is 0.
   The fraction returned by this function is always in reduced form
   (see documentation for reduce).
*/
fraction_t *make_fraction(int a, int b)
{
    fraction_t *pf = malloc(sizeof(fraction_t));
    if (b == 0)
    {
        printf ("Error, dividing by zero");
        exit(0);
    }
    (*pf).num = a;
    (*pf).den = b;
    reduce(pf);
}

/* Return a pointer to a new fraction containing the sum of the fractions
   pointed to by pf1 and pf2.
   The fraction returned by this function is always in reduced form
   (see documentation for reduce).
   Terminate the program via assert() if pf1 or pf2 is a NULL pointer.
*/
fraction_t *add_fractions(fraction_t *pf1, fraction_t *pf2)
{
    fraction_t *pf = make_fraction(0, 1);
    return pf;
}

/* Return a pointer to a new fraction containing the product of the fractions
   pointed to by pf1 and pf2.
   The fraction returned by this function is always in reduced form
   (see documentation for reduce).
   Terminate the program via assert() if pf1 or pf2 is a NULL pointer.
*/
fraction_t *multiply_fractions(fraction_t *pf1, fraction_t *pf2)
{
    fraction_t *pf = make_fraction(0, 1);
    return pf;
}
