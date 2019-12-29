package com.tyfanch.dynamicjs.oldengine.test;

import com.tyfanch.dynamicjs.oldengine.annotation.ScriptParam;

public interface JsFileRunner {
    void showHello();

    Integer evalPlus(Integer a, Integer b);

    Double evalPow(@ScriptParam("a") Integer a, @ScriptParam("b") Integer b);

    Double evalSin(double a, @ScriptParam("b") double b);
}
