package org.tyfanchz.common.properties;

import java.util.Map;
import java.util.Properties;

/**
 * <p>Description: TyzPropertiesUtils
 * <p>加载 {@code .properties}文件的工具类。
 *
 * <p>USAGE：
 * <p>&emsp;1. 编写配置类，实现{@link TyzPropertiesConfigParent}的方法；
 * <p>&emsp;2. 编写properties枚举类，实现{@link TyzPropertiesParent}的方法；
 * <p>&emsp;3. 在项目启动时使用{@link TyzPropertiesUtils#loadConfig(Class)}加载步骤1中的配置类；
 * <p>&emsp;4. 在需要使用properties的地方使用步骤2中的枚举类，调用实现的{@link TyzPropertiesParent#get()}方法来获取属性值。
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public class TyzPropertiesUtils {
    public static final String PROPERTIES_PREFIX = "/";
    public static final String PROPERTIES_SUFFIX = ".properties";

    private TyzPropertiesUtils() {}

    public static void loadConfig(Class<? extends TyzPropertiesConfigParent> configClass) {
        TyzPropertiesConfigParent config;
        Map<Class<?>, String> configMap;

        try {
            config = configClass.newInstance();
            configMap = config.getConfigMap();

            for (Map.Entry<Class<?>, String> entry : configMap.entrySet()) {
                Class<?> clazz = entry.getKey();
                String filename = entry.getValue();
                String trimmedFilename;
                String fullFilename;
                Properties properties;

                // 掐头去尾
                trimmedFilename = filename
                    .replaceAll("^" + PROPERTIES_PREFIX, "")
                    .replaceAll("\\" + PROPERTIES_SUFFIX + "$", "");
                // 重新组合
                fullFilename = PROPERTIES_PREFIX + trimmedFilename + PROPERTIES_SUFFIX;
                properties = load(fullFilename);

                TyzPropertiesStore.STORE.put(clazz.getName(), properties);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Properties load(String filename) {
        Properties properties = new Properties();

        try {
            properties.load(TyzPropertiesUtils.class.getResourceAsStream(filename));
        } catch (Exception e) {
            System.err.println("Cannot load " + filename);
        }

        return properties;
    }

    public static String get(Class<?> clazz, String propKey) {
        Properties properties;
        String propValue;

        properties = TyzPropertiesStore.STORE.get(clazz.getName());
        propValue = properties.getProperty(propKey);

        return propValue;
    }
}
