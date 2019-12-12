#include <stdio.h>
#include <windows.h>
#include <winsock.h>
#define ICO_MAIN 0
#define ID_TIMER 10

LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
	char *cName = TEXT("Wnd1");
	char *cCaption = TEXT("Lation W.Pro");
	HWND hWnd;
	MSG msg;
	WNDCLASSEX wc;
	
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;
	wc.cbSize = sizeof(WNDCLASSEX);
	wc.style = CS_HREDRAW | CS_VREDRAW;
	wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	wc.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(ICO_MAIN));
	wc.hIconSm = LoadIcon(hInstance, MAKEINTRESOURCE(ICO_MAIN));
	wc.hCursor = LoadCursor(NULL, MAKEINTRESOURCE(IDC_ARROW));
	wc.hInstance = hInstance;
	wc.lpfnWndProc = WndProc;
	wc.lpszClassName = cName;
	wc.lpszMenuName = NULL;
	RegisterClassEx(&wc);
	hWnd = CreateWindowEx(WS_EX_CLIENTEDGE, cName, cCaption, WS_OVERLAPPEDWINDOW, 300, 200, CW_USEDEFAULT, CW_USEDEFAULT, NULL, NULL, hInstance, NULL);
	if(hWnd == NULL)
	{
		MessageBox(NULL, TEXT("Cannot create a window!\n"), TEXT("Error"), MB_ICONERROR);
		return 0;
	}
	ShowWindow(hWnd, nShowCmd);
	UpdateWindow(hWnd);
	while(GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return msg.wParam;
}




LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	HDC hDC;
	RECT rect;
	PAINTSTRUCT ps;
	char tmp[100];
	//int iWidth, iHeight;
	static int x = 0, y = 0;
	switch(msg)
	{
	case WM_CREATE:
		GetClientRect(hWnd, &rect);
		sprintf(tmp, "%ld\t%ld\n%ld\t%ld", rect.left, rect.right, rect.top, rect.bottom);
		MessageBox(hWnd, tmp, TEXT("Info"), MB_OK);
		SetTimer(hWnd, ID_TIMER, 100, NULL);
		return 0;
	/*case WM_PAINT:
		hDC = BeginPaint(hWnd, &ps);
		GetClientRect(hWnd, &rect);
		DrawText(hDC, TEXT("Hello world!!\n"), -1, &rect, DT_CENTER);
		EndPaint(hWnd, &ps);
		return 0;
	case WM_LBUTTONUP:
		GetWindowRect(hWnd, &rect);
		MessageBox(hWnd, TEXT("Click 'OK' to move the window to (0, 0).\n"), TEXT("Info"), MB_OK);
		iWidth = rect.right - rect.left;
		iHeight = rect.bottom - rect.top;
		if(rect.left < 50)
		{
			rect.left = 800;
			rect.right = iWidth + 800;
		}
		for(; rect.left > 0; rect.left -= 2, rect.right -= 2) MoveWindow(hWnd, rect.left, 0, iWidth, iHeight, TRUE);
		return 0;*/
	/*case WM_TIMER:
		hDC = GetDC(hWnd);
		Rectangle(hDC, x, y, x + 10, y + 10);
		//TextOut(hDC, x, y, TEXT("Me"), 2);
		x += 5;
		y += 5;
		ReleaseDC(hWnd, hDC);
		return 0;*/
	case WM_MOUSEMOVE:
		if (wParam & MK_LBUTTON)
		{
			hDC = GetDC(hWnd);
			Rectangle(hDC, x % 600, y % 600, x % 600 + 32, y % 600 + 32);
			//TextOut(hDC, x, y, TEXT("Me"), 2);
			x += 6;
			y += 5;
			ReleaseDC(hWnd, hDC);
		}
		return 0;
	case WM_DESTROY:
		PostQuitMessage(0);
		return 0;
	}
	return DefWindowProc(hWnd, msg, wParam, lParam);
}
