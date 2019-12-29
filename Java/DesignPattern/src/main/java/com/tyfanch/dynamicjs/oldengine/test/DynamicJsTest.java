package com.tyfanch.dynamicjs.oldengine.test;

import com.tyfanch.dynamicjs.oldengine.script.DefaultScriptRunnerFactory;
import com.tyfanch.dynamicjs.oldengine.script.ScriptRunnerFactory;

public class DynamicJsTest {
    public static void main(String[] args) {
        testJsFileRunner();
        testJsAnnotationRunner();
    }

    private static void testJsAnnotationRunner() {
        ScriptRunnerFactory scriptRunnerFactory = new DefaultScriptRunnerFactory();
        JsAnnotationRunner runner;

        System.out.println("$$$$ testJsAnnotationRunner");
        runner = scriptRunnerFactory.getByClass(JsAnnotationRunner.class);
        System.out.println(runner.calMul(23.9, 123.4));
        System.out.println(runner.calDiv(108.0, 24.6));
        runner.formatStr("aaa", "vbbb", "ME");
    }

    private static void testJsFileRunner() {
        ScriptRunnerFactory scriptRunnerFactory = new DefaultScriptRunnerFactory();
        JsFileRunner runner;

        System.out.println("$$$$ testJsFileRunner");
        runner = scriptRunnerFactory.getByNamespace(JsFileRunner.class);
        runner.showHello();
        System.out.println(runner.evalPlus(4, 5));
        System.out.println(runner.evalPow(2, 10));
        runner.evalSin(30.0, 2.0f);
    }
}
