#=========================
# Created by Woobhurk.
# All Rights Reserved.
# Copyright(C)2012.
#=========================

cFile = test.c
oFile = test.o test_res.o
sFile = test.s
exeFile = test.exe
rcFile = Res.rc

initial:
	@echo Generating Assembly Files...
	@gcc -S $(cFile)
	@echo Compiling...
	@windres $(rcFile) test_res.o
	@gcc -Wall -g -c $(cFile)
	@echo Linking...
	@gcc -Wall -s -o $(exeFile) $(oFile) -mwindows -lwsock32
	@echo Any key to run...
	@pause>NUL
	@cls
	@$(exeFile)

final:
	@echo Compiling...
	@windres $(rcFile) test_res.o
	@gcc -Wall -c $(cFile)
	@echo Linking...
	@gcc -Wall -o $(exeFile) $(oFile) -mwindows -lwsock32

debug:
	@gdb $(exeFile)

clean:
	@del $(oFile) $(sFile) $(exeFile)
