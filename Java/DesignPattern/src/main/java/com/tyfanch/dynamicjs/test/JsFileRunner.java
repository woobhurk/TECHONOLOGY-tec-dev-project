package com.tyfanch.dynamicjs.test;

import com.tyfanch.dynamicjs.annotation.ScriptParam;

public interface JsFileRunner {
    void showHello();

    Integer evalPlus(Integer a, Integer b);

    Double evalPow(@ScriptParam("a") Integer a, @ScriptParam("b") Integer b);

    Double evalSin(double a, @ScriptParam("b") double b);
}
