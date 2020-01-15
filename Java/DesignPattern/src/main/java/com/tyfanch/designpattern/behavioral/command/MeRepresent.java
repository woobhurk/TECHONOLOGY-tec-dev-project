package com.tyfanch.designpattern.behavioral.command;

public class MeRepresent implements Represent {
    @Override
    public void action(Command command) {
        command.execute();
    }
}
