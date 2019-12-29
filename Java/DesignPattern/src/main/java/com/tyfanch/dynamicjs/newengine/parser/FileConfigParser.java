package com.tyfanch.dynamicjs.newengine.parser;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import com.tyfanch.dynamicjs.newengine.config.ScriptConfigFactory;
import com.tyfanch.dynamicjs.newengine.model.ScriptConfig;
import com.tyfanch.dynamicjs.utils.JsonUtils;

/**
 * 通过文件解析脚本配置
 *
 * @deprecated 暂时停止维护
 */
public class FileConfigParser implements ConfigParser {
    // 配置文件名
    private String configFile;
    // 脚本配置
    private ScriptConfig scriptConfig;

    /**
     * 必须传入配置文件名
     *
     * @param configFile 配置文件名
     */
    public FileConfigParser(String configFile) {
        this.configFile = configFile;
    }

    @Override
    public ScriptConfig parseScriptConfig() {
        InputStream inputStream = ScriptConfigFactory.class.getResourceAsStream(
            this.configFile);
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        StringBuilder stringBuilder = new StringBuilder();
        String configFileContent;

        reader.lines().forEach(s -> stringBuilder.append(s).append("\n"));
        configFileContent = stringBuilder.toString();
        this.scriptConfig = JsonUtils.fromJson(configFileContent, ScriptConfig.class);

        return this.scriptConfig;
    }
}
