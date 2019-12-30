package com.tyfanch.dynamicscript.enginev2.factory;

import com.tyfanch.dynamicscript.enginev2.config.ScriptConfigFactory;
import com.tyfanch.dynamicscript.enginev2.model.ScriptConfig;

/**
 * 可运行实例工厂的公共实现类
 */
public abstract class BaseScriptRunnerFactory implements ScriptRunnerFactory {
    @Override
    public <T> T getByClass(Class<T> tClass) {
        ScriptConfig scriptConfig;
        T runnerProxy;

        scriptConfig = ScriptConfigFactory.readFromClass(tClass);
        runnerProxy = this.getRunnerProxy(scriptConfig, tClass);

        return runnerProxy;
    }

    @Override
    public <T> T getByNamespace(Class<T> tClass) {
        ScriptConfig scriptConfig;
        T runnerProxy;

        scriptConfig = ScriptConfigFactory.readFromNamespace(tClass);
        runnerProxy = this.getRunnerProxy(scriptConfig, tClass);

        return runnerProxy;
    }

    protected abstract  <T> T getRunnerProxy(ScriptConfig scriptConfig, Class<T> tClass);
}
