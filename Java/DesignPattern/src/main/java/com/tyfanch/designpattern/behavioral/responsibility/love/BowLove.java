package com.tyfanch.designpattern.behavioral.responsibility.love;

import com.tyfanch.designpattern.behavioral.responsibility.action.LoveAction;

/**
 * <p>Description:
 *
 * <p>Project: DesignPattern
 *
 * @author tyfanchz
 * @date 2020-04-07
 */
public class BowLove implements Love {
    @Override
    public LoveAction getLoveAction() {
        return LoveAction.BOW;
    }

    @Override
    public void wellIWantToDo() {
        System.out.println("想去抱住小甜心~");
    }
}
