package com.tyfanch.designpattern.creational.prototype;

public class AdMailTemplate implements MailTemplate {
    @Override
    public String getSubject() {
        return AdMailConfig.SUBJECT;
    }

    @Override
    public String getContent() {
        return AdMailConfig.CONTENT;
    }
}
