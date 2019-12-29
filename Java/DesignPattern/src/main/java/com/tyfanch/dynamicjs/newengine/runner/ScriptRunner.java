package com.tyfanch.dynamicjs.newengine.runner;

import java.lang.reflect.Method;

/**
 * 脚本运行器，提供脚本运行的总方法
 * 脚本运行包括：
 * - 编译脚本
 * - 执行脚本
 */
public interface ScriptRunner {
    /**
     * 运行脚本
     *
     * @param method 要运行的方法
     * @param args 参数
     * @return 运行结果
     * @throws Exception 错误
     */
    Object run(Method method, Object... args) throws Exception;
}
