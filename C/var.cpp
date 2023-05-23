#include <stdio.h>"

int integer = 1;
float fl = 1.0;
char character = L'c';
short court = 12;
long longue = 2147483647;
bool boolean = true;
double dble = 1728937281382176.0;
unsigned long long int usignedll = 0;

unsigned long long int get_usignedll()
{
	scanf_s("%llu", &usignedll);
	return usignedll;
}

int main()
{
	printf("char: %c\n", character);
	printf("char size: %zi\n", sizeof(character));
	printf("int: %i\n", integer);
	printf("float: %f\n", fl);
	printf("bool: %d\n", boolean);
	printf("long: %li\n", longue);
	printf("double: %f\n", dble);
	printf("short: %d\n", court);
	get_usignedll();
	if (usignedll > 18446744073709551614)
	{
		printf("Taille maximum\n");
	}
	else {
		printf("OK\n");
	}
	printf("unsigned long long int: %llu\n", usignedll);

	//printf("size of usignedll: %i\n", sizeof(usignedll));
	switch (sizeof(usignedll))
	{
	case 1:
		printf("usignedll = 1 bit\n");
		break;
	case 2:
		printf("usignedll = 2 bit\n");
		break;
	case 3:
		printf("usignedll = 3 bit\n");
		break;
	case 4:
		printf("usignedll = 4 bit\n");
		break;
	case 5:
		printf("usignedll = 5 bit\n");
		break;
	case 6:
		printf("usignedll = 6 bit\n");
		break;
	case 7:
		printf("usignedll = 7 bit\n");
		break;
	case 8:
		printf("usignedll = 8 bit\n");
		break;
	default:
		printf("Invalide.\n");
	}
	return 0;
}