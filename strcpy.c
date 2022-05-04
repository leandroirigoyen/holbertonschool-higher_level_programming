#include "main.h"
char *_strcpy(char *dest, char *src)
{
	int i;
	
	for(;src[i] != '\0'; i++)
	{
		dest[i] = src[i];
	}
	dest[i] = src[i];

return (dest);
}
