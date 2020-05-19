package org.tyfanchz.common.properties;

import java.util.Map;

/**
 * <p>Description: TyzPropertiesConfigParent
 *
 * <p>配置类接口，所有配置类需要实现该接口。
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public interface TyzPropertiesConfigParent {
    /**
     * 获取配置类的Map，key为properties枚举类的Class，value为properties文件名
     *
     * @return 配置类的Map
     */
    Map<Class<?>, String> getConfigMap();
}
