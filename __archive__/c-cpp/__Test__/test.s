	.file	"test.c"
	.globl	_pos_b
	.data
	.align 64
_pos_b:
	.long	-1
	.space 39996
	.globl	_search_str
	.section .rdata,"dr"
LC0:
	.ascii "bing\0"
	.data
	.align 4
_search_str:
	.long	LC0
	.text
	.globl	_set_pos_b
	.def	_set_pos_b;	.scl	2;	.type	32;	.endef
_set_pos_b:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$36, %esp
	.cfi_offset 3, -12
	movl	$0, -12(%ebp)
	movl	$0, -16(%ebp)
	jmp	L2
L4:
	movl	-12(%ebp), %edx
	movl	8(%ebp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %edx
	movl	_search_str, %eax
	movzbl	(%eax), %eax
	cmpb	%al, %dl
	jne	L3
	movl	-16(%ebp), %eax
	leal	1(%eax), %edx
	movl	%edx, -16(%ebp)
	movl	-12(%ebp), %edx
	movl	%edx, _pos_b(,%eax,4)
L3:
	addl	$1, -12(%ebp)
L2:
	movl	-12(%ebp), %ebx
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_strlen
	cmpl	%eax, %ebx
	jb	L4
	addl	$36, %esp
	popl	%ebx
	.cfi_restore 3
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.globl	_count_char
	.def	_count_char;	.scl	2;	.type	32;	.endef
_count_char:
LFB14:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$52, %esp
	.cfi_offset 3, -12
	movl	12(%ebp), %eax
	movb	%al, -28(%ebp)
	movl	$0, -12(%ebp)
	movl	$0, -16(%ebp)
	jmp	L6
L8:
	movl	-12(%ebp), %edx
	movl	8(%ebp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %eax
	cmpb	-28(%ebp), %al
	jne	L7
	addl	$1, -16(%ebp)
L7:
	addl	$1, -12(%ebp)
L6:
	movl	-12(%ebp), %ebx
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_strlen
	cmpl	%eax, %ebx
	jb	L8
	movl	-16(%ebp), %eax
	addl	$52, %esp
	popl	%ebx
	.cfi_restore 3
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE14:
	.section .rdata,"dr"
LC1:
	.ascii "1   %d %d\12\0"
LC2:
	.ascii "2   %d %d\12\0"
LC3:
	.ascii "3-1 %d %d\12\0"
LC4:
	.ascii "3-2 %d %d\12\0"
	.text
	.globl	_count_bing
	.def	_count_bing;	.scl	2;	.type	32;	.endef
_count_bing:
LFB15:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$36, %esp
	.cfi_offset 3, -12
	movl	$0, -12(%ebp)
	movl	16(%ebp), %ebx
	movl	_search_str, %eax
	movl	%eax, (%esp)
	call	_strlen
	cmpl	%eax, %ebx
	jne	L11
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_printf
	movl	$0, 16(%ebp)
	movl	$1, %eax
	jmp	L12
L11:
	movl	12(%ebp), %ebx
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_strlen
	cmpl	%eax, %ebx
	jne	L13
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC2, (%esp)
	call	_printf
	movl	$0, %eax
	jmp	L12
L13:
	movl	12(%ebp), %edx
	movl	8(%ebp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %edx
	movl	_search_str, %ecx
	movl	16(%ebp), %eax
	addl	%ecx, %eax
	movzbl	(%eax), %eax
	cmpb	%al, %dl
	jne	L14
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC3, (%esp)
	call	_printf
	movl	16(%ebp), %eax
	leal	1(%eax), %edx
	movl	12(%ebp), %eax
	addl	$1, %eax
	movl	%edx, 8(%esp)
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_count_bing
	addl	%eax, -12(%ebp)
	jmp	L15
L14:
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC4, (%esp)
	call	_printf
	movl	12(%ebp), %eax
	leal	1(%eax), %edx
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	%edx, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_count_bing
	addl	%eax, -12(%ebp)
L15:
	movl	-12(%ebp), %eax
L12:
	addl	$36, %esp
	popl	%ebx
	.cfi_restore 3
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE15:
	.section .rdata,"dr"
LC5:
	.ascii "0\0"
	.def	___moddi3;	.scl	2;	.type	32;	.endef
	.text
	.globl	_fun
	.def	_fun;	.scl	2;	.type	32;	.endef
_fun:
LFB16:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$52, %esp
	.cfi_offset 3, -12
	movl	%esp, %eax
	movl	%eax, %ebx
	movl	$0, -16(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_strlen
	movl	%eax, %edx
	subl	$1, %edx
	movl	%edx, -20(%ebp)
	movl	$16, %edx
	subl	$1, %edx
	addl	%edx, %eax
	movl	$16, %ecx
	movl	$0, %edx
	divl	%ecx
	imull	$16, %eax, %eax
	call	___chkstk_ms
	subl	%eax, %esp
	leal	16(%esp), %eax
	addl	$0, %eax
	movl	%eax, -24(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_set_pos_b
	movl	_pos_b, %eax
	cmpl	$-1, %eax
	jne	L17
	movl	$0, %eax
	jmp	L18
L17:
	movl	_pos_b, %eax
	movl	%eax, %edx
	movl	8(%ebp), %eax
	addl	%eax, %edx
	movl	-24(%ebp), %eax
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	_strcpy
	movl	%eax, -28(%ebp)
	movl	$0, -12(%ebp)
	jmp	L19
L20:
	movl	$LC5, (%esp)
	call	_puts
	movl	-12(%ebp), %eax
	movl	_pos_b(,%eax,4), %eax
	leal	1(%eax), %edx
	movl	-24(%ebp), %eax
	movl	$1, 8(%esp)
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	_count_bing
	addl	%eax, -16(%ebp)
	addl	$1, -12(%ebp)
L19:
	movl	_search_str, %eax
	movzbl	(%eax), %eax
	movsbl	%al, %edx
	movl	-24(%ebp), %eax
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	_count_char
	cmpl	-12(%ebp), %eax
	jg	L20
	movl	-16(%ebp), %eax
	cltd
	movl	$1410065415, 8(%esp)
	movl	$2, 12(%esp)
	movl	%eax, (%esp)
	movl	%edx, 4(%esp)
	call	___moddi3
L18:
	movl	%ebx, %esp
	movl	-4(%ebp), %ebx
	leave
	.cfi_restore 5
	.cfi_restore 3
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE16:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC6:
	.ascii "binbning\0"
LC7:
	.ascii "num = %d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB17:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$LC6, (%esp)
	call	_fun
	movl	%eax, 4(%esp)
	movl	$LC7, (%esp)
	call	_printf
	call	_getch
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE17:
	.ident	"GCC: (i686-posix-dwarf-rev0, Built by MinGW-W64 project) 4.9.2"
	.def	_strlen;	.scl	2;	.type	32;	.endef
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_strcpy;	.scl	2;	.type	32;	.endef
	.def	_puts;	.scl	2;	.type	32;	.endef
	.def	_getch;	.scl	2;	.type	32;	.endef
