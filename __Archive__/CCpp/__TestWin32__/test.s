	.file	"test.c"
	.section .rdata,"dr"
LC0:
	.ascii "Wnd1\0"
LC1:
	.ascii "Lation W.Pro\0"
LC2:
	.ascii "Error\0"
LC3:
	.ascii "Cannot create a window!\12\0"
	.text
	.globl	_WinMain@16
	.def	_WinMain@16;	.scl	2;	.type	32;	.endef
_WinMain@16:
LFB86:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$152, %esp
	movl	$LC0, -12(%ebp)
	movl	$LC1, -16(%ebp)
	movl	$0, -84(%ebp)
	movl	$0, -80(%ebp)
	movl	$48, -96(%ebp)
	movl	$3, -92(%ebp)
	movl	$0, (%esp)
	movl	__imp__GetStockObject@4, %eax
	call	*%eax
	subl	$4, %esp
	movl	%eax, -64(%ebp)
	movl	$0, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__LoadIconA@8, %eax
	call	*%eax
	subl	$8, %esp
	movl	%eax, -72(%ebp)
	movl	$0, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__LoadIconA@8, %eax
	call	*%eax
	subl	$8, %esp
	movl	%eax, -52(%ebp)
	movl	$32512, 4(%esp)
	movl	$0, (%esp)
	movl	__imp__LoadCursorA@8, %eax
	call	*%eax
	subl	$8, %esp
	movl	%eax, -68(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, -76(%ebp)
	movl	$_WndProc@16, -88(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -56(%ebp)
	movl	$0, -60(%ebp)
	leal	-96(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__RegisterClassExA@4, %eax
	call	*%eax
	subl	$4, %esp
	movl	$0, 44(%esp)
	movl	8(%ebp), %eax
	movl	%eax, 40(%esp)
	movl	$0, 36(%esp)
	movl	$0, 32(%esp)
	movl	$-2147483648, 28(%esp)
	movl	$-2147483648, 24(%esp)
	movl	$200, 20(%esp)
	movl	$300, 16(%esp)
	movl	$13565952, 12(%esp)
	movl	-16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	-12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$512, (%esp)
	movl	__imp__CreateWindowExA@48, %eax
	call	*%eax
	subl	$48, %esp
	movl	%eax, -20(%ebp)
	cmpl	$0, -20(%ebp)
	jne	L2
	movl	$16, 12(%esp)
	movl	$LC2, 8(%esp)
	movl	$LC3, 4(%esp)
	movl	$0, (%esp)
	movl	__imp__MessageBoxA@16, %eax
	call	*%eax
	subl	$16, %esp
	movl	$0, %eax
	jmp	L6
L2:
	movl	20(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	-20(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__ShowWindow@8, %eax
	call	*%eax
	subl	$8, %esp
	movl	-20(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__UpdateWindow@4, %eax
	call	*%eax
	subl	$4, %esp
	jmp	L4
L5:
	leal	-48(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__TranslateMessage@4, %eax
	call	*%eax
	subl	$4, %esp
	leal	-48(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__DispatchMessageA@4, %eax
	call	*%eax
	subl	$4, %esp
L4:
	movl	$0, 12(%esp)
	movl	$0, 8(%esp)
	movl	$0, 4(%esp)
	leal	-48(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__GetMessageA@16, %eax
	call	*%eax
	subl	$16, %esp
	testl	%eax, %eax
	jne	L5
	movl	-40(%ebp), %eax
L6:
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret	$16
	.cfi_endproc
LFE86:
	.section .rdata,"dr"
LC4:
	.ascii "%ld\11%ld\12%ld\11%ld\0"
LC5:
	.ascii "Info\0"
	.text
	.globl	_WndProc@16
	.def	_WndProc@16;	.scl	2;	.type	32;	.endef
_WndProc@16:
LFB87:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	pushl	%esi
	pushl	%ebx
	subl	$236, %esp
	.cfi_offset 7, -12
	.cfi_offset 6, -16
	.cfi_offset 3, -20
	movl	12(%ebp), %eax
	cmpl	$2, %eax
	je	L9
	cmpl	$512, %eax
	je	L10
	cmpl	$1, %eax
	jne	L15
	leal	-44(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__GetClientRect@8, %eax
	call	*%eax
	subl	$8, %esp
	movl	-32(%ebp), %ebx
	movl	-40(%ebp), %ecx
	movl	-36(%ebp), %edx
	movl	-44(%ebp), %eax
	movl	%ebx, 20(%esp)
	movl	%ecx, 16(%esp)
	movl	%edx, 12(%esp)
	movl	%eax, 8(%esp)
	movl	$LC4, 4(%esp)
	leal	-208(%ebp), %eax
	movl	%eax, (%esp)
	call	_sprintf
	movl	$0, 12(%esp)
	movl	$LC5, 8(%esp)
	leal	-208(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__MessageBoxA@16, %eax
	call	*%eax
	subl	$16, %esp
	movl	$0, 12(%esp)
	movl	$100, 8(%esp)
	movl	$10, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__SetTimer@16, %eax
	call	*%eax
	subl	$16, %esp
	movl	$0, %eax
	jmp	L14
L10:
	movl	16(%ebp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	je	L13
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__GetDC@4, %eax
	call	*%eax
	subl	$4, %esp
	movl	%eax, -28(%ebp)
	movl	_y.60409, %ecx
	movl	$458129845, %edx
	movl	%ecx, %eax
	imull	%edx
	sarl	$6, %edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	imull	$600, %eax, %eax
	subl	%eax, %ecx
	movl	%ecx, %eax
	leal	32(%eax), %edi
	movl	_x.60408, %ecx
	movl	$458129845, %edx
	movl	%ecx, %eax
	imull	%edx
	sarl	$6, %edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	imull	$600, %eax, %eax
	subl	%eax, %ecx
	movl	%ecx, %eax
	leal	32(%eax), %esi
	movl	_y.60409, %ebx
	movl	$458129845, %edx
	movl	%ebx, %eax
	imull	%edx
	sarl	$6, %edx
	movl	%ebx, %eax
	sarl	$31, %eax
	movl	%edx, %ecx
	subl	%eax, %ecx
	imull	$600, %ecx, %eax
	subl	%eax, %ebx
	movl	%ebx, %ecx
	movl	_x.60408, %ebx
	movl	$458129845, %edx
	movl	%ebx, %eax
	imull	%edx
	sarl	$6, %edx
	movl	%ebx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	imull	$600, %eax, %eax
	subl	%eax, %ebx
	movl	%ebx, %eax
	movl	%edi, 16(%esp)
	movl	%esi, 12(%esp)
	movl	%ecx, 8(%esp)
	movl	%eax, 4(%esp)
	movl	-28(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__Rectangle@20, %eax
	call	*%eax
	subl	$20, %esp
	movl	_x.60408, %eax
	addl	$6, %eax
	movl	%eax, _x.60408
	movl	_y.60409, %eax
	addl	$5, %eax
	movl	%eax, _y.60409
	movl	-28(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__ReleaseDC@8, %eax
	call	*%eax
	subl	$8, %esp
L13:
	movl	$0, %eax
	jmp	L14
L9:
	movl	$0, (%esp)
	movl	__imp__PostQuitMessage@4, %eax
	call	*%eax
	subl	$4, %esp
	movl	$0, %eax
	jmp	L14
L15:
	movl	20(%ebp), %eax
	movl	%eax, 12(%esp)
	movl	16(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	movl	__imp__DefWindowProcA@16, %eax
	call	*%eax
	subl	$16, %esp
L14:
	leal	-12(%ebp), %esp
	popl	%ebx
	.cfi_restore 3
	popl	%esi
	.cfi_restore 6
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret	$16
	.cfi_endproc
LFE87:
.lcomm _y.60409,4,4
.lcomm _x.60408,4,4
	.ident	"GCC: (i686-posix-dwarf-rev0, Built by MinGW-W64 project) 4.9.2"
	.def	_sprintf;	.scl	2;	.type	32;	.endef
