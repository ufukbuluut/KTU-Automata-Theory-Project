
%{
#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
FILE *dosya;	//OUTPUT DOSYASI
FILE *hatadosyasi; //Hata dosyasý
FILE* input = NULL; //Giriþlerin olduðu Txt metin


int sym[26]; 

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char*message);

int i=1;

%}



%union 
{
	int num; 
	char id;
}


%token T_NEWLINE
%token <id> DONGU
%token <id> TURN
%token <id> STEP
%token <num>  SAYI
%token <id> LSB
%token <id> RSB
%token<id> RENK
%token<id> BACKWARD

%type <num> ASGN LOOP ILERI SAG PEN

%start bas


%%

bas:
	|bas line
;

line: IFADE T_NEWLINE 
		{

		printf("%i. Satir Okundu.......\n",i);
		i++;
		//fprintf(dosya,"*\n");
		}

;

IFADE: |ASGN IFADE   
;


ASGN : 

	|STEP SAYI
		{
			$$=1;
			fprintf(dosya,"F%i\n",$2);
		}
	|LOOP SAYI{$$=2;}
	|TURN SAYI 
		{
			$$=3;
			fprintf(dosya,"R%i\n",$2);
		}
	|ILERI 
	{
			fprintf(dosya,"ILERI\n");
		}
	|BACKWARD SAYI
		{
			$$=4;
			fprintf(dosya,"B%i\n",$2);
		}	

|LOOP LSB IFADE RSB {fprintf(dosya,"L%i\n",$2);}
|PEN{;}
|RENK 'M'{fprintf(dosya,"CM\n");}
|RENK 'K'{fprintf(dosya,"CK\n");}
|RENK 'Y'{fprintf(dosya,"CY\n");}
|RENK 'S'{fprintf(dosya,"CS\n");}



;

PEN:
|'P''E''N' SAYI
{
	$$=$4;
	if($4==1)
	{
	fprintf(dosya,"P1\n");
	}

	if($4==2)
	{
	fprintf(dosya,"P2\n");
	}

	if($4==3)
	{
	fprintf(dosya,"P3\n");
	}
	if($4!=1 && $4!=2 && $4!=3)
	{
	printf("ERROR! -> GECERSIZ KALEM KALINLIGI");
	fprintf(hatadosyasi,"ERROR!: GECERSIZ KALEM KALINLIGI");
	}
}
;



LOOP : DONGU SAYI

{
	$$ =$2;
	//printf(" L %i \n",$2);
	
}
;

ILERI: STEP SAYI 
{
	$$ = $2;
	//printf(" F %i \n",$2);
}
;

SAG: TURN
{
	//printf(" R %i \n");
}
;




%%

int main() {
	//yyin = stdin;

	fopen_s(&input, "Inputs.txt", "rb");


	yyin = input;
	dosya=fopen("Outputs.txt","w");
	hatadosyasi=fopen("Errors.txt","w");

	yyparse();
		fclose(dosya);
		fclose(hatadosyasi);

	return 0;
}

void yyerror(const char* s) {
	fprintf(hatadosyasi,"Parse error: %s\n", s);
	fprintf(stderr, "Parse error: %s\n", s);
	exit(1);
}

