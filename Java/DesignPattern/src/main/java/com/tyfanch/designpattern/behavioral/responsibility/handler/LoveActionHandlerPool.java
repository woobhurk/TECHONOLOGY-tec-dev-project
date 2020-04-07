package com.tyfanch.designpattern.behavioral.responsibility.handler;

/**
 * <p>Description:
 *
 * <p>Project: DesignPattern
 *
 * @author tyfanchz
 * @date 2020-04-07
 */
public enum  LoveActionHandlerPool {
    SEE_ACTION(new SeeLoveActionHandler()),
    BOW_ACTION(new BowLoveActionHandler()),
    KISS_ACTION(new KissLoveActionHandler()),
    GO_ACTION(new GoLoveActionHandler()),
    ;

    private LoveActionHandler loveActionHandler;

    LoveActionHandlerPool(LoveActionHandler loveActionHandler) {
        this.loveActionHandler = loveActionHandler;
    }

    public LoveActionHandler getLoveActionHandler() {
        return this.loveActionHandler;
    }
}
