package com.tyfanch.designpattern.behavioral.responsibility.action;

import com.tyfanch.designpattern.behavioral.responsibility.handler.BowLoveActionHandler;
import com.tyfanch.designpattern.behavioral.responsibility.handler.GoLoveActionHandler;
import com.tyfanch.designpattern.behavioral.responsibility.handler.KissLoveActionHandler;
import com.tyfanch.designpattern.behavioral.responsibility.handler.LoveActionHandler;
import com.tyfanch.designpattern.behavioral.responsibility.handler.SeeLoveActionHandler;

/**
 * <p>Description:
 *
 * <p>Project: DesignPattern
 *
 * @author tyfanchz
 * @date 2020-04-07
 */
public enum LoveAction {
    SEE(new SeeLoveActionHandler()),
    BOW(new BowLoveActionHandler()),
    KISS(new KissLoveActionHandler()),
    GO(new GoLoveActionHandler());

    private LoveActionHandler loveActionHandler;

    LoveAction(LoveActionHandler loveActionHandler) {
        this.loveActionHandler = loveActionHandler;
    }

    public LoveActionHandler get() {
        return this.loveActionHandler;
    }
}
