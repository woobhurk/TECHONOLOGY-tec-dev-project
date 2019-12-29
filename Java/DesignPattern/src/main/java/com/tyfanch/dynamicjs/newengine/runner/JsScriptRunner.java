package com.tyfanch.dynamicjs.newengine.runner;

import java.lang.reflect.Method;
import java.util.Map;
import com.tyfanch.dynamicjs.newengine.compiler.DefaultScriptProcessor;
import com.tyfanch.dynamicjs.newengine.compiler.ScriptProcessor;
import com.tyfanch.dynamicjs.newengine.executor.JsScriptExecutor;
import com.tyfanch.dynamicjs.newengine.executor.ScriptExecutor;
import com.tyfanch.dynamicjs.newengine.model.MethodConfig;
import com.tyfanch.dynamicjs.newengine.model.ScriptConfig;

/**
 * JavaScript脚本运行器
 */
public class JsScriptRunner extends BaseScriptRunner {
    // 脚本处理器
    private ScriptProcessor scriptProcessor;
    // 脚本执行器
    private ScriptExecutor scriptExecutor;
    // 脚本配置
    private ScriptConfig scriptConfig;
    // 执行脚本的引擎名称
    private String engineName;
    // 编译后的脚本
    private String compiledScript;

    /**
     * 必须传入脚本配置
     *
     * @param scriptConfig 脚本配置
     */
    public JsScriptRunner(ScriptConfig scriptConfig) {
        this.scriptConfig = scriptConfig;
    }

    //public JsScriptRunner(ConfigParser configParser) {
    //    this.configParser = configParser;
    //}

    @Override
    public Object run(Method method, Object... args) throws Exception {
        Object result;

        this.compiledScript = this.processScript(method, args);
        result = this.executeScript(method);

        return result;
    }

    //@Override
    //protected ScriptConfig parseScriptConfig() {
    //    // 每个脚本配置只需要解析一次
    //    if (this.scriptConfig == null) {
    //        this.scriptConfig = this.configParser.parseScriptConfig();
    //    }
    //
    //    return this.scriptConfig;
    //}

    @Override
    protected String processScript(Method method, Object... args) {
        Map<String, MethodConfig> methodConfigMap = this.scriptConfig.getMethods();
        MethodConfig methodConfig = methodConfigMap.get(method.getName());
        String script;

        if (methodConfig == null) {
            String errorMsg = String.format(
                "Method `%s` in `%s` has no implementation in configuration",
                method.getName(), this.scriptConfig.getNamespace());

            throw new RuntimeException(errorMsg);
        }

        script = methodConfig.getScript();
        this.scriptProcessor = new DefaultScriptProcessor(method);
        this.engineName = methodConfig.getEngine();
        this.compiledScript = this.scriptProcessor.formatAndCompile(script, args);

        return this.compiledScript;
    }

    @Override
    protected Object executeScript(Method method) throws Exception {
        this.scriptExecutor = new JsScriptExecutor();
        this.scriptExecutor.execute(this.engineName, this.compiledScript);

        return null;
    }
}
