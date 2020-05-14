/*
* Filename:	LTLib.h
* Author:	Lation.Woobhurk
* Date:		2013.01.04
* Comment:	This header file defines some usual macros.
* Last modified time: 2013.01.05
*
* All Rights Reserved.
*/

/*----------------------------------------------------------*/
/*Logic-----------------------------------------------------*/
#define	AND	&&
#define	OR	||
#define	NOT	!
#define	BUT	&&  /* ^_^ */

/*----------------------------------------------------------*/
/*Assembly--------------------------------------------------*/


/*----------------------------------------------------------*/
/*Assert----------------------------------------------------*/
#include <stdlib.h>
#include <windows.h>  /*Used to call MessageBox function*/

void _ASSERT(char *, int);

#ifdef NODEBUG
	#define ASSERTFILE NULL
	#define ASSERT(exp) NULL
#else
	#define ASSERTFILE static char *AssertName = __FILE__;  /*This macro must be called at first*/
	#define ASSERT(exp) \
	if(exp) \
		NULL; \
	else \
		_ASSERT(AssertName, __LINE__)


	void _ASSERT(char *filename, int linenum)
	{
		char ErrInfo[512];

		sprintf(ErrInfo, "File: %s, Line: %d\nExpression wasn't established.\n\nContinue or not?\n[Yes] I want to continue.\n[No] Don't continue, and then quit.", filename, linenum);
		if(MessageBox(NULL, ErrInfo, "Error", MB_YESNO | MB_DEFBUTTON2 | MB_ICONERROR) == IDNO) exit(1);
	}
#endif
