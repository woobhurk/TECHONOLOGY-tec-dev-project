package com.tyfanch.dynamicjs.newengine.test;

import com.tyfanch.dynamicjs.newengine.annotation.ScriptParam;

public interface JsFileRunner {
    void showHello();

    Integer evalPlus(Integer a, Integer b);

    Double evalPow(@ScriptParam("a") Integer a, @ScriptParam("b") Integer b);

    Double evalSin(double a, @ScriptParam("b") double b);
}
