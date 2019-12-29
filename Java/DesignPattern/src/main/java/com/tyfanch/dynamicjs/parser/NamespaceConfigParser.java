package com.tyfanch.dynamicjs.parser;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Map;
import com.tyfanch.dynamicjs.config.ScriptConfigFactory;
import com.tyfanch.dynamicjs.model.MethodConfig;
import com.tyfanch.dynamicjs.model.ScriptConfig;
import com.tyfanch.dynamicjs.utils.JsonUtils;

/**
 * 从命名空间对应的配置文件读取Script配置
 */
public class NamespaceConfigParser implements ConfigParser {
    private String namespace;

    /**
     * 命名空间，必须指定
     * @param namespace 命名空间
     */
    public NamespaceConfigParser(String namespace) {
        this.namespace = namespace;
    }

    /**
     * 命名空间对应的类
     * @param tClass 类
     */
    public NamespaceConfigParser(Class<?> tClass) {
        this.namespace = tClass.getName();
    }

    @Override
    public ScriptConfig parseScriptConfig() {
        InputStream configFileInputStream;
        String configFileContent;
        ScriptConfig scriptConfig;

        configFileInputStream = this.getConfigFileInputStream();
        configFileContent = this.getConfigFileContent(configFileInputStream);
        scriptConfig = this.getScriptConfigByStream(configFileContent);

        return scriptConfig;
    }

    /**
     * 获取配置文件输入流，如果文件不存在则抛出异常
     * @return 配置文件输入流
     */
    private InputStream getConfigFileInputStream() {
        String configFilePath;
        InputStream configFileInputStream;

        configFilePath = "/" + this.namespace.replace(".", "/") + ".json";
        configFileInputStream = ScriptConfigFactory.class.getResourceAsStream(
            configFilePath);

        if (configFileInputStream == null) {
            String errorMsg = String.format(
                "No corresponding configuration file found (%s) for namespace `%s`",
                configFilePath, this.namespace);

            throw new RuntimeException(errorMsg);
        }

        return configFileInputStream;
    }

    /**
     * 从输入流中读取Script配置文件内容
     * @param inputStream 输入流
     * @return 读取到的Script配置文件内容
     */
    private String getConfigFileContent(InputStream inputStream) {
        BufferedReader reader;
        StringBuilder configFileContentSb;
        String configFileContent;

        reader = new BufferedReader(new InputStreamReader(inputStream));
        configFileContentSb = new StringBuilder();

        reader.lines().forEach(s -> configFileContentSb.append(s).append("\n"));
        configFileContent = configFileContentSb.toString();

        return configFileContent;
    }

    /**
     * 从文件内容中解析Script配置
     * @param configFileContent 文件内容
     * @return Script配置
     */
    private ScriptConfig getScriptConfigByStream(String configFileContent) {
        ScriptConfig scriptConfig;

        scriptConfig = JsonUtils.fromJson(configFileContent, ScriptConfig.class);

        if (scriptConfig == null) {
            String errorMsg = String.format(
                "Error when parsing configuration file corresponding to namespace `%s`",
                this.namespace
            );

            throw new RuntimeException(errorMsg);
        }

        // 如果配置里面没有命名空间则自动设置
        if (scriptConfig.getNamespace() == null
            || scriptConfig.getNamespace().trim().isEmpty()) {
            scriptConfig.setNamespace(this.namespace);
        }

        // 将未设置引擎的方法自动设置引擎为Script配置的引擎
        for (Map.Entry<String, MethodConfig> entry : scriptConfig.getMethods().entrySet()) {
            MethodConfig methodConfig = entry.getValue();

            if (methodConfig.getEngine() == null
                || methodConfig.getEngine().trim().isEmpty()) {
                methodConfig.setEngine(scriptConfig.getEngine());
            }
        }

        return scriptConfig;
    }
}
