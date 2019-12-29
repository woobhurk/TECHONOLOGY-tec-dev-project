package com.tyfanch.dynamicjs.newengine.compiler;

import java.text.MessageFormat;

/**
 * 使用MessageText来格式化脚本
 */
public class MessageScriptFormatter implements ScriptFormatter {
    @Override
    public String format(String script, Object... args) {
        String formattedScript;

        formattedScript = MessageFormat.format(script, args);

        return formattedScript;
    }
}
