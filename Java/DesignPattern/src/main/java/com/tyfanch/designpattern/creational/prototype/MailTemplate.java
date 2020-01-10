package com.tyfanch.designpattern.creational.prototype;

import java.io.Serializable;

public class MailTemplate implements Serializable, Cloneable {
    private String subject;
    private String receiver;

    public String getSubject() {
        return this.subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getReceiver() {
        return this.receiver;
    }

    public void setReceiver(String receiver) {
        this.receiver = receiver;
    }

    @Override
    public String toString() {
        return "MailTemplate{" +
            "subject='" + this.subject + '\'' +
            ", receiver='" + this.receiver + '\'' +
            '}';
    }
}
