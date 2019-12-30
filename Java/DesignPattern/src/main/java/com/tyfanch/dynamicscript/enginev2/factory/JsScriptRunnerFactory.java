package com.tyfanch.dynamicscript.enginev2.factory;

import java.lang.reflect.Proxy;
import com.tyfanch.dynamicscript.enginev2.handler.JsScriptRunnerHandler;
import com.tyfanch.dynamicscript.enginev2.handler.ScriptRunnerHandler;
import com.tyfanch.dynamicscript.enginev2.model.ScriptConfig;

/**
 * 默认的实例化可运行接口的工厂
 */
@SuppressWarnings("unchecked")
public class JsScriptRunnerFactory extends BaseScriptRunnerFactory {
    // 运行控制类
    private ScriptRunnerHandler scriptRunnerHandler;

    /**
     * 获取可运行实例（代理）
     * @param tClass 类
     * @param <T> 可运行实例的类型
     * @return 获取到的可运行实例的代理
     */
    @Override
    protected  <T> T getRunnerProxy(ScriptConfig scriptConfig, Class<T> tClass) {
        T runnerProxy;

        this.scriptRunnerHandler = new JsScriptRunnerHandler(scriptConfig);
        runnerProxy = (T) Proxy.newProxyInstance(
            ClassLoader.getSystemClassLoader(),
            new Class[]{tClass},
            this.scriptRunnerHandler);

        return runnerProxy;
    }
}
