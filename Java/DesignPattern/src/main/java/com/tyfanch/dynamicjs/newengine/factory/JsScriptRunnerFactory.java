package com.tyfanch.dynamicjs.newengine.factory;

import java.lang.reflect.Proxy;
import com.tyfanch.dynamicjs.newengine.config.ScriptConfigFactory;
import com.tyfanch.dynamicjs.newengine.handler.JsScriptRunnerHandler;
import com.tyfanch.dynamicjs.newengine.handler.ScriptRunnerHandler;
import com.tyfanch.dynamicjs.newengine.model.ScriptConfig;

/**
 * 默认的实例化可运行接口的工厂
 */
@SuppressWarnings("unchecked")
public class JsScriptRunnerFactory implements ScriptRunnerFactory {
    // 脚本配置
    private ScriptConfig scriptConfig;
    // 运行控制类
    private ScriptRunnerHandler scriptRunnerHandler;

    @Override
    public <T> T getByClass(Class<T> tClass) {
        T runnerProxy;

        this.scriptConfig = ScriptConfigFactory.readFromClass(tClass);
        runnerProxy = this.getRunnerProxy(tClass);

        return runnerProxy;
    }

    @Override
    public <T> T getByNamespace(Class<T> tClass) {
        T runnerProxy;

        this.scriptConfig = ScriptConfigFactory.readFromNamespace(tClass);
        runnerProxy = this.getRunnerProxy(tClass);

        return runnerProxy;
    }

    /**
     * 获取可运行实例（代理）
     * @param tClass 类
     * @param <T> 可运行实例的类型
     * @return 获取到的可运行实例的代理
     */
    private <T> T getRunnerProxy(Class<T> tClass) {
        T runnerProxy;

        this.scriptRunnerHandler = new JsScriptRunnerHandler(this.scriptConfig);
        runnerProxy = (T) Proxy.newProxyInstance(
            ClassLoader.getSystemClassLoader(),
            new Class[]{tClass},
            this.scriptRunnerHandler);

        return runnerProxy;
    }
}
