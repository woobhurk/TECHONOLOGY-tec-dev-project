package org.tyfanchz.common.properties;

/**
 * <p>Description: TyzPropertiesParent
 *
 * <p>properties枚举类的接口，所有properties枚举类都需要实现该接口。
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public interface TyzPropertiesParent {
    /**
     * 获取properties的key
     *
     * @return key
     */
    String getPropKey();

    /**
     * 获取properties的value
     *
     * @return value
     */
    default String get() {
        String propValue;

        // 间接使用TyzPropertiesUtils来获取value
        propValue = TyzPropertiesUtils.get(this.getClass(), this.getPropKey());

        return propValue;
    }
}
