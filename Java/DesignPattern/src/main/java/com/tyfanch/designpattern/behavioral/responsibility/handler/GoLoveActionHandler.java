package com.tyfanch.designpattern.behavioral.responsibility.handler;

import com.tyfanch.designpattern.behavioral.responsibility.action.LoveAction;
import com.tyfanch.designpattern.behavioral.responsibility.love.Love;

/**
 * <p>Description:
 *
 * <p>Project: DesignPattern
 *
 * @author tyfanchz
 * @date 2020-04-07
 */
public class GoLoveActionHandler implements LoveActionHandler {
    @Override
    public boolean proceed(Love love) {
        love.wellIWantToDo();
        System.out.println("和小甜心回家去咯！");

        return true;
    }

    @Override
    public LoveActionHandler getNext() {
        return null;
    }

    @Override
    public void setNext(LoveActionHandler nextHandler) {

    }

    @Override
    public LoveAction getLoveAction() {
        return LoveAction.GO;
    }
}
