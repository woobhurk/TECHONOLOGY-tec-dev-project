package com.tyfanch.dynamicjs.newengine.compiler;

/**
 * 脚本处理器
 * 用于综合处理脚本的格式化和编译
 */
public interface ScriptProcessor extends ScriptFormatter, ScriptCompiler {
    /**
     * 格式化+编译脚本
     *
     * @param script 脚本
     * @param args 参数
     * @return 格式化+编译后的脚本
     */
    default String formatAndCompile(String script, Object... args) {
        String formattedScript;
        String compiledScript;

        formattedScript = this.format(script, args);
        compiledScript = this.compile(formattedScript, args);

        return compiledScript;
    }
}
