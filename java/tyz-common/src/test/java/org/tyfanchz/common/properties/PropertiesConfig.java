package org.tyfanchz.common.properties;

import java.util.HashMap;
import java.util.Map;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public class PropertiesConfig implements TyzPropertiesConfigParent {
    private static final Map<Class<?>, String> CONFIG_MAP = new HashMap<>();

    static {
        CONFIG_MAP.put(AaaProperties.class, "test");
        CONFIG_MAP.put(BbbProperties.class, "new-test.properties");
    }

    @Override
    public Map<Class<?>, String> getConfigMap() {
        return CONFIG_MAP;
    }
}
