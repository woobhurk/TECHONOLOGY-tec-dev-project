#=========================
# Created by Woobhurk.
# All Rights Reserved.
# Copyright(C)2012.
#=========================

cFile = test.c
oFile = test.o
sFile = test.s
exeFile = test.exe

initial:
	@echo Generating Assembly Files...
	@gcc -S $(cFile)
	@echo Compling...
	@gcc -Wall -g -c $(cFile)
	@echo Linking...
	@gcc -Wall -s -o $(exeFile) $(oFile)
	@echo Any key to run...
	@pause>NUL
	@cls
	@$(exeFile)

final:
	@echo Compling...
	@gcc -Wall -c $(cFile)
	@echo Linking...
	@gcc -Wall -o $(exeFile) $(oFile)

debug:
	@gdb $(exeFile)

clean:
	@del $(oFile) $(sFile) $(exeFile)
