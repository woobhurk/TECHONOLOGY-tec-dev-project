package com.tyfanch.designpattern.creational.prototype;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class Mail implements Serializable, Cloneable {
    private String subject;
    private String receiver;
    private String content;

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

    public String getContent() {
        return this.content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    @Override
    protected Object clone() {
        Mail clonedMail;
        ByteArrayOutputStream byteArrayOutputStream;
        ObjectOutputStream objectOutputStream;
        ByteArrayInputStream byteArrayInputStream;
        ObjectInputStream objectInputStream;

        try {
            // 浅拷贝
            //clonedMail = (Mail) super.clone();

            // 深拷贝
            // 写入输出流
            byteArrayOutputStream = new ByteArrayOutputStream();
            objectOutputStream = new ObjectOutputStream(byteArrayOutputStream);
            objectOutputStream.writeObject(byteArrayOutputStream);
            // 从输出流读取
            byteArrayInputStream = new ByteArrayInputStream(byteArrayOutputStream.toByteArray());
            objectInputStream = new ObjectInputStream(byteArrayInputStream);
            clonedMail = (Mail) objectInputStream.readObject();
        } catch (Exception e) {
            clonedMail = null;
            e.printStackTrace();
        }

        return clonedMail;
    }

    @Override
    public String toString() {
        return "Mail{" +
            "subject='" + this.subject + '\'' +
            ", receiver='" + this.receiver + '\'' +
            ", content='" + this.content + '\'' +
            '}';
    }
}
