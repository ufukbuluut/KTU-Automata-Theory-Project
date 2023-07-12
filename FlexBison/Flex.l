%option noyywrap

%{
#include <stdio.h>

#define YY_DECL int yylex()

#include "Bison.tab.h"
#define fileno _fileno
%}

%%

[ \t]	; // ignore all whitespace
[0-9]+		{yylval.id = atoi(yytext); return SAYI;}
\n		{return T_NEWLINE;}
"L"		{return DONGU;}
"["		{return LSB;}
"]"		{return RSB;}
"R"		{return TURN;}
"F"		{return STEP;}
"COLOR" {return RENK;}
"B"     {return BACKWARD;}
[A-Z] return *yytext;
%%