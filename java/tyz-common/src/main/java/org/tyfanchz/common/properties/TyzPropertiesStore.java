package org.tyfanchz.common.properties;

import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

/**
 * <p>Description: TyzPropertiesStore
 *
 * <p>只有一个作用：存储所有已加载的properties，存放到Map中。
 * <p>Map的key为properties枚举类的Class，value为加载的properties数据。
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public class TyzPropertiesStore {
    private TyzPropertiesStore() {}

    public static final Map<String, Properties> STORE = new HashMap<>();
}
