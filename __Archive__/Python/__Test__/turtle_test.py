#encoding = utf-8
import turtle

#turtle.hideturtle();
turtle.speed("slowest");
turtle.bgcolor("#f08000");
#turtle.bgpic("E:\\Program Folder\\Gif录制工具\\a.gif");
turtle.penup();
turtle.goto(100, 100);
turtle.pendown();
turtle.goto(20, 190);
turtle.write("H1");
turtle.forward(5);
turtle.write("H2");
turtle.setworldcoordinates(-turtle.window_width() / 8, -turtle.window_height() / 2, turtle.window_width() / 8, turtle.window_height() / 2);
#turtle.setworldcoordinates(-2, -1, 2, 1);
turtle.pendown()
turtle.goto(0, 0);
turtle.write("New Coordinates");
turtle.goto(10, 10);
cv = turtle.getcanvas();
print(cv);
