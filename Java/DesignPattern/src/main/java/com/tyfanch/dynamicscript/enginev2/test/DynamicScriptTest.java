package com.tyfanch.dynamicscript.enginev2.test;

import com.tyfanch.dynamicscript.enginev2.factory.JsScriptRunnerFactory;
import com.tyfanch.dynamicscript.enginev2.factory.ScriptRunnerFactory;

public class DynamicScriptTest {
    public static void main(String[] args) {
        testJsFileRunner();
        System.out.println("----");
        testJsAnnotationRunner();
    }

    private static void testJsAnnotationRunner() {
        ScriptRunnerFactory scriptRunnerFactory = new JsScriptRunnerFactory();
        JsAnnotationRunner runner;

        System.out.println("$$$$ testJsAnnotationRunner");
        runner = scriptRunnerFactory.getByClass(JsAnnotationRunner.class);
        System.out.println(runner.calMul(23.9, 123.4));
        System.out.println(runner.calDiv(108.0, 24.6));
        runner.formatStr("aaa", "vbbb", "ME");
    }

    private static void testJsFileRunner() {
        ScriptRunnerFactory scriptRunnerFactory = new JsScriptRunnerFactory();
        JsFileRunner runner;

        System.out.println("$$$$ testJsFileRunner");
        runner = scriptRunnerFactory.getByNamespace(JsFileRunner.class);
        runner.showHello();
        System.out.println(runner.evalPlus(4, 5));
        System.out.println(runner.evalPow(2, 10));
        runner.evalSin(30.0, 2.0f);
    }
}
