package com.tyfanch.designpattern.behavioral.responsibility;

import com.tyfanch.designpattern.behavioral.responsibility.handler.LoveActionHandler;
import com.tyfanch.designpattern.behavioral.responsibility.handler.LoveActionHandlerPool;
import com.tyfanch.designpattern.behavioral.responsibility.love.GoLove;

/**
 * <p>Description:
 *
 * <p>Project: DesignPattern
 *
 * @author tyfanchz
 * @date 2020-04-07
 */
public class ResponsibilityTest {
    public static void main(String[] args) {
        testResponsibility();
    }

    private static void testResponsibility() {
        LoveActionHandler loveActionHandler;

        loveActionHandler = LoveActionHandlerPool.SEE_ACTION.getLoveActionHandler();
        loveActionHandler.handle(new GoLove());
    }
}
