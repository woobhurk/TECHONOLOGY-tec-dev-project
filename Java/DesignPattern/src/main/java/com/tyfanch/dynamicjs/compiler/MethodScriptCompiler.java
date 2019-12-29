package com.tyfanch.dynamicjs.compiler;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;
import com.tyfanch.dynamicjs.annotation.ScriptParam;
import com.tyfanch.dynamicjs.utils.TemplateStringUtils;

/**
 * 通过高级参数替换来编译脚本，即通过方法中的注解来替换参数
 */
public class MethodScriptCompiler implements ScriptCompiler {
    private Method method;

    /**
     * 必须指定方法
     * @param method 方法
     */
    public MethodScriptCompiler(Method method) {
        this.method = method;
    }

    @Override
    public String compile(String script, Object... args) {
        Map<String, Object> paramMap;
        String compiledString;

        paramMap = this.buildParamMap(args);
        compiledString = this.compileByParamMap(script, paramMap);

        return compiledString;
    }

    /**
     * 建立注解中参数名和参数值的映射关系，生成Map
     * @param args 传入的参数
     * @return 建立的映射关系的Map
     */
    private Map<String, Object> buildParamMap(Object... args) {
        Annotation[][] allParamAnnotations = this.method.getParameterAnnotations();
        Map<String, Object> paramMap = new HashMap<>();

        if (allParamAnnotations != null) {
            for (int i = 0; i < allParamAnnotations.length; i++) {
                Annotation[] perParamAnnotations = allParamAnnotations[i];
                String paramName = this.getParamNameInAnnotations(perParamAnnotations);

                if (paramName != null) {
                    paramMap.put(paramName, args[i]);
                }
            }
        }

        return paramMap;
    }

    /**
     * 获取单个参数中ScriptParam注解的值，即参数名
     * @param annotations 单个参数的所有注解
     * @return 如果有注解则返回参数名，如果没有返回null
     */
    private String getParamNameInAnnotations(Annotation[] annotations) {
        String paramName = null;

        for (Annotation annotation : annotations) {
            if (annotation instanceof ScriptParam) {
                String value = ((ScriptParam) annotation).value().trim();
                String name = ((ScriptParam) annotation).name().trim();

                if (value.isEmpty() && name.isEmpty()) {
                    String errorMsg = String.format(
                        "Parameter name error: `%s` and `%s`",
                        value, name
                    );

                    throw new RuntimeException(errorMsg);
                }

                paramName = value.isEmpty() ? name : value;
                break;
            }
        }

        return paramName;
    }

    /**
     * 通过参数名和参数值的映射关系来编译脚本
     * @param script 要编译的脚本
     * @param paramMap 映射关系的Map
     * @return 编译后的脚本
     */
    private String compileByParamMap(String script, Map<String, Object> paramMap) {
        //String compiledScript = script;
        //
        //for (Map.Entry<String, Object> entry : paramMap.entrySet()) {
        //    String paramName = entry.getKey();
        //    Object paramValue = entry.getValue();
        //
        //    // 正则替换
        //    // (?!\\)zzz：zzz前面不包含\\的字符，不会匹配到前面的字符
        //    // 如果使用[^\\]zzz则会匹配到zzz前面的一个字符，如azzz、bzzz因此替换会出错
        //    // "(?!\\\\)\\$\\{ *" + paramName + " *}"转义后实际上就是
        //    // (?!\\)\$\{ *... *}
        //    compiledScript = compiledScript.replaceAll(
        //        "([^\\\\])\\$\\{ *" + paramName + " *}",
        //        "\\1" + String.valueOf(paramValue));
        //}
        //
        //return compiledScript;
        String compiledScript;

        compiledScript = TemplateStringUtils.processByFreemarker(script, paramMap);

        return compiledScript;
    }
}
