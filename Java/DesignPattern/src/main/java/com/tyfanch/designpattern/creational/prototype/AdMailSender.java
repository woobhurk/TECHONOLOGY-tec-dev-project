package com.tyfanch.designpattern.creational.prototype;

import java.util.Random;

public class AdMailSender implements MailSender {
    private Random random = new Random(System.currentTimeMillis());
    private MailTemplate mailTemplate = new MailTemplate();
    private Mail mail = new Mail();

    @Override
    public boolean send(Mail mail) {
        this.mailTemplate.setReceiver("Receiver" + this.random.nextInt(999));
        this.mailTemplate.setSubject("Subject" + this.random.nextInt(999));


        return false;
    }
}
