#include <stdio.h>
#include <conio.h>
#include <string.h>

#define CB 0
#define CI 1
#define CN 2
#define CG 3

int pos[4][10000];

void set_pos(char *s)
{
	int cnt, posn;
	
	for (cnt = 0, posn = 0; cnt < stlen(s); cnt++)
	{
		if (s[cnt] == 'b') pos[CB][posn++];
	}
	
	for (cnt = 0, posn = 0; cnt < stlen(s); cnt++)
	{
		if (s[cnt] == 'i') pos[CI][posn++];
	}
	
	for (cnt = 0, posn = 0; cnt < stlen(s); cnt++)
	{
		if (s[cnt] == 'n') pos[CN][posn++];
	}
	
	for (cnt = 0, posn = 0; cnt < stlen(s); cnt++)
	{
		if (s[cnt] == 'g') pos[CG][posn++];
	}
}

int count_char(char *s, char c)
{
	int cnt, posn;
	
	for (posn = 0, cnt = 0; posn < strlen(s); posn++)
	{
		if (s[posn] == c)
		{
			++cnt;
		}
	}
	return cnt;
}

int count_bing(char *s)
{
	int posn, bing_num = 0;
	
	for (posn = 0; posn < count_char(s, 'b'); posn++)
	{
		bi_num
	}
	
	return bing_num;
}

int fun(char *s)
{
	int bing_num = 0, cnt;
	char tmp_s[strlen(s)];
	char *startp;
	
	if (count_char(s, 'b') == 0 || count_char(s, 'i') == 0 || count_char(s, 'n') == 0 || count_char(s, 'g') == 0) return 0;
	
	set_pos(s);
	strcpy(tmp_s, s);
	startp = strcpy(tmp_s, tmp_s + pos[CB][0]);
	
	bing_num = count_bing(tmp_s);
	
	return bing_num;
}

int main(void)
{
	printf("num = %d\n", count_char("bibinngg", 'g'));
	getch();
	return 0;
}
