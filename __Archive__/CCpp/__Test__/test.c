#include <stdio.h>
#include <conio.h>
#include <string.h>

int pos_b[10000] = {-1};
char *search_str = "bing";

void set_pos_b(char *s)
{
	int posn1, posn2;
	
	for (posn1 = 0, posn2 = 0; posn1 < strlen(s); posn1++)
	{
		if (s[posn1] == search_str[0])
		{
			pos_b[posn2++] = posn1;
		}
	}
}

int count_char(char *s, char c)
{
	int cnt, c_num;
	
	for (cnt = 0, c_num= 0; cnt < strlen(s); cnt++)
	{
		if (s[cnt] == c)
		{
			++c_num;
		}
	}
	return c_num;
}

int count_bing(char *s, int s_pos, int s_s_pos)
{
	int cnt = 0;
	
	if (s_s_pos == strlen(search_str))
	{
		printf("1   %d %d\n", s_pos, s_s_pos);
		s_s_pos = 0;
		return 1;
	}
	if (s_pos == strlen(s))
	{
		printf("2   %d %d\n", s_pos, s_s_pos);
		return 0;
	}
	
	if (s[s_pos] == search_str[s_s_pos])
	{
		printf("3-1 %d %d\n", s_pos, s_s_pos);
		//++s_pos;
		//++s_s_pos;
		cnt += count_bing(s, s_pos + 1, s_s_pos + 1);
	}
	else
	{
		printf("3-2 %d %d\n", s_pos, s_s_pos);
		//++s_pos;
		cnt += count_bing(s, s_pos + 1, s_s_pos);
	}
	//cnt += count_bing(s, s_pos, s_s_pos);
	
	return cnt;
}

int fun(char *s)
{
	int posn, bing_num = 0;
	char tmp_s[strlen(s)];
	char *startp;
	
	set_pos_b(s);
	if (pos_b[0] == -1)
	{
		return 0;
	}
	
	startp = strcpy(tmp_s, s + pos_b[0]);
	
	for (posn = 0; posn < count_char(tmp_s, search_str[0]); posn++)
	{
		puts("0");
		bing_num += count_bing(tmp_s, pos_b[posn] + 1, 1);
	}
	
	return bing_num % 10000000007;
}

int main(void)
{
	printf("num = %d\n", fun("binbning"));
	getch();
	return 0;
}
