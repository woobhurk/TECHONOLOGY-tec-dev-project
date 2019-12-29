package com.tyfanch.dynamicjs.newengine.handler;

import java.lang.reflect.Method;
import com.tyfanch.dynamicjs.newengine.model.ScriptConfig;
import com.tyfanch.dynamicjs.newengine.runner.JsScriptRunner;
import com.tyfanch.dynamicjs.newengine.runner.ScriptRunner;

/**
 * JavaScript可运行实例的控制类
 */
public class JsScriptRunnerHandler implements ScriptRunnerHandler {
    // 脚本配置
    private ScriptConfig scriptConfig;
    // 脚本运行器
    private ScriptRunner scriptRunner;

    /**
     * 必须传入Script配置
     *
     * @param scriptConfig Script配置
     */
    public JsScriptRunnerHandler(ScriptConfig scriptConfig) {
        this.scriptConfig = scriptConfig;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Exception {
        Object result;

        // 判断方法从何处声明，用来区分用户自定义方法和JDK自带方法
        if (Object.class.equals(method.getDeclaringClass())) {
            // 方法是从Object继承过来的
            result = method.invoke(this, args);
        } else {
            // 方法是接口定义的，运行脚本
            result = this.runScript(method, args);
        }

        return result;
    }

    /**
     * 运行方法对应的脚本
     *
     * @param method 要运行的方法
     * @param args 方法参数
     * @return 运行结果
     * @throws Exception 异常
     */
    private Object runScript(Method method, Object... args) throws Exception {
        Object result;

        this.scriptRunner = new JsScriptRunner(this.scriptConfig);
        result = this.scriptRunner.run(method, args);

        return result;
    }
}
