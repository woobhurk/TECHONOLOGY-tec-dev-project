package com.tyfanch.designpattern.creational.prototype;

public class AdMailSender implements MailSender {
    @Override
    public boolean send(Mail mail) {
        System.out.println("Sending " + mail);

        return true;
    }
}
