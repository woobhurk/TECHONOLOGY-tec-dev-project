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
public interface LoveActionHandler {
    default boolean handle(Love love) {
        boolean result;

        if (love.getLoveAction().equals(this.getLoveAction())) {
            result = this.proceed(love);
        } else {
            if (this.getNext() != null) {
                result = this.getNext().handle(love);
            } else {
                System.out.println("做完咯~");
                result = false;
            }
        }

        return result;
    }

    boolean proceed(Love love);

    LoveActionHandler getNext();

    void setNext(LoveActionHandler nextHandler);

    LoveAction getLoveAction();
}
