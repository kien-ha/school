/* SYSC 2006 Winter 2015, Lab 2, Part 2. */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#include "sput.h"

/* By default, Pelles C generates "warning #2154: Unreachable code"
   and "warning #2130: Result of comparison is constant" when the
   macros in sput.h are used. The following pragma directive disables the
   generation of these warnings.
 */
#pragma warn(disable: 2130 2154)

/* ----  Do not change any of the statements above this line. --------- */

/* Exercise 1. */

/* Return the largest of the n doubles in arr[].
 * This function assumes that parameter n is >= 1.
 */
double max(double arr[], int n)
{
    double maximum = arr[0];
    int i = 0;
    for (i; i < n; i += 1)
    {
        if (maximum < arr[i])
            maximum = arr[i];
    }
    return maximum;
}

/* Exercise 2. */

/* Return the smallest of the n doubles in arr[].
 * This function assumes that parameter n is >= 1.
 */
double min(double arr[], int n)
{
    double minimum = arr[0];
    int i = 0;
    for (i; i < n; i += 1)
    {
        if (arr[i] < minimum)
            minimum = arr[i];
    }
	return minimum;
}

/* Exercise 3. */

/* Normalize the n doubles in x[].
 * This function assumes that parameter n is >= 2, and that at least
 * two of the values in x[] are different.
 */
void normalize(double x[], int n)
{
    int i = 0;
    double maxx=max(x, n);
    double minn = min(x, n);
    for (i; i<n; i+=1)
    {
        x[i] = (x[i] - minn)/(maxx - minn);
    }
}

/* Exercise 4. */

/* Return the average magnitude of the n doubles in x[].
 * This function assumes that parameter n is >= 1.
 */
double avg_magnitude(double x[], double n)
{
    double sum = 0;
	int i = 0;
    for (i; i<n; i+=1)
        sum = fabs(x[i]) + sum;
    return sum / n;
}

/* Exercise 5. */

/* Return the average power of the n doubles in x[].
 * This function assumes that parameter n is >= 1.
 */
double avg_power(double x[], double n)
{
	int i = 0;
    double squared_sum = 0;
    for (i; i < n; i += 1)
        squared_sum += pow(x[i], 2);
    return squared_sum / n;
}


/*---------------------------------------------------------------------------
 * Test harness for this lab. Do not modify any of the code below this line.
 */

static void test_max(void)
{
    double data1[] = {1.0, 2.0, 3.0, 4.0};
	double data2[] = {1.0, 2.0, 4.0, 3.0};
	double data3[] = {4.0, 3.0, 2.0, 1.0};
	double data4[] = {5.0};
	double data5[] = {2.0, 2.0};

    sput_fail_unless(fabs(max(data1, 4) - 4.0) < 0.001,
                     "max({1.0, 2.0, 3.0, 4.0}) ==> 4.0");
    sput_fail_unless(fabs(max(data2, 4) - 4.0) < 0.001,
                     "max({1.0, 2.0, 4.0, 3.0}) ==> 4.0");
    sput_fail_unless(fabs(max(data3, 4) - 4.0) < 0.001,
                     "max({4.0, 3.0, 2.0, 1.0}) ==> 4.0");
    sput_fail_unless(fabs(max(data4, 1) - 5.0) < 0.001,
                     "max({5.0}) ==> 5.0");
    sput_fail_unless(fabs(max(data5, 2) - 2.0) < 0.001,
                     "max({2.0, 2.0}) ==> 2.0");
}

static void test_min(void)
{
    double data1[] = {1.0, 2.0, 3.0, 4.0};
	double data2[] = {2.0, 1.0, 4.0, 3.0};
	double data3[] = {4.0, 3.0, 2.0, 1.0};
	double data4[] = {5.0};
	double data5[] = {2.0, 2.0};

    sput_fail_unless(fabs(min(data1, 4) - 1.0) < 0.001,
                     "min({1.0, 2.0, 3.0, 4.0}) ==> 1.0");
    sput_fail_unless(fabs(min(data2, 4) - 1.0) < 0.001,
                     "min({2.0, 1.0, 4.0, 3.0}) ==> 1.0");
    sput_fail_unless(fabs(min(data3, 4) - 1.0) < 0.001,
                     "min({4.0, 3.0, 2.0, 1.0}) ==> 1.0");
    sput_fail_unless(fabs(min(data4, 1) - 5.0) < 0.001,
                     "min({5.0}) ==> 5.0");
    sput_fail_unless(fabs(min(data5, 2) - 2.0) < 0.001,
                     "min({2.0, 2.0}) ==> 2.0");
}

static _Bool compare_arrays(double arr1[], double arr2[], int n)
{
    for (int i = 0; i < n; i = i + 1) {
        if (fabs(arr1[i] - arr2[i]) > 0.001) {
            return false;
        }
    }
    return true;
}

static void test_normalize(void)
{
	double samples[] = {-2.0, -1.0, 2.0, 0.0};
    double expected[] = {0.0, 0.25, 1.0, 0.5};

    normalize(samples, 4);

    sput_fail_unless(compare_arrays(samples, expected, 4),
                     "\nnormalize({-2.0, -1.0, 2.0, 0.0}) ==> "
                     "{0.0, 0.25, 1.0, 0.5}");
}

static void test_avg_magnitude(void)
{
    double samples[] = {5.7, 2.3, -1.9, 4.5, 6.2, -8.1, 9.7, 3.1};

    sput_fail_unless(fabs(avg_magnitude(samples, 8) - 5.19) < 0.01,
                     "\navg_magnitude({5.7, 2.3, -1.9, 4.5, 6.2, -8.1, "
                     "9.7, 3.1}, 8) ==> 5.19");
}

static void test_avg_power(void)
{
    double samples[] = {5.7, 2.3, -1.9, 4.5, 6.2, -8.1, 9.7, 3.1};

    sput_fail_unless(fabs(avg_power(samples, 8) - 33.67) < 0.01,
                     "\navg_power({5.7, 2.3, -1.9, 4.5, 6.2, -8.1, "
                     "9.7, 3.1}, 8) ==> 33.67");
}

int main(void)
{
    sput_start_testing();

    sput_enter_suite("Exercise 1: max()");
    sput_run_test(test_max);

    sput_enter_suite("Exercise 2: min()");
    sput_run_test(test_min);

    sput_enter_suite("Exercise 3: normalize()");
    sput_run_test(test_normalize);

    sput_enter_suite("Exercise 4: avg_magnitude()");
    sput_run_test(test_avg_magnitude);

    sput_enter_suite("Exercise 5: avg_power()");
    sput_run_test(test_avg_power);

    sput_finish_testing();
    return sput_get_return_value();
}
