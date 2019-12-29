package com.tyfanch.dynamicjs.newengine.runner;

import java.lang.reflect.Method;

/**
 * 脚本运行器抽象类
 * 定义脚本运行的几个步骤：编译、执行
 */
public abstract class BaseScriptRunner implements ScriptRunner {
    ///**
    // * 解析脚本配置
    // *
    // * @return 脚本配置
    // */
    //protected abstract ScriptConfig parseScriptConfig();

    /**
     * 处理脚本
     * 处理过程包括格式化和编译
     *
     * @param method 要处理的方法
     * @param args 参数
     * @return 处理后的脚本语句
     */
    protected abstract String processScript(Method method, Object... args);

    /**
     * 执行脚本
     *
     * @param method 要执行的方法
     * @return 执行结果
     * @throws Exception 错误
     */
    protected abstract Object executeScript(Method method) throws Exception;
}
