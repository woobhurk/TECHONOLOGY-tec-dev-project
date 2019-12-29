package com.tyfanch.dynamicjs.compiler;

/**
 * 脚本编译类，编译方式由子类决定
 */
public interface ScriptCompiler {
    /**
     * 编译脚本，编译的内容包括参数替换等
     * @param script 脚本
     * @param args 参数
     * @return 编译后的脚本
     */
    String compile(String script, Object... args);
}
