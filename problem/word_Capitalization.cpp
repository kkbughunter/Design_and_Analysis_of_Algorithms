#include<iostream>
using namespace std;
int main()
{
	char word[10000];
	cin >> word;
	word[0] = toupper(word[0]);
	printf("%s\n", word);
	return 0;
}
