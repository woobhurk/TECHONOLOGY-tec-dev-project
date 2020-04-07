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
public class BowLoveActionHandler implements LoveActionHandler {
    @Override
    public boolean proceed(Love love) {
        love.wellIWantToDo();
        System.out.println("赶紧冲过去抱住小甜心~~");

        return true;
    }

    @Override
    public LoveActionHandler getNext() {
        return LoveActionHandlerPool.KISS_ACTION.getLoveActionHandler();
    }

    @Override
    public LoveAction getLoveAction() {
        return LoveAction.BOW;
    }
}
