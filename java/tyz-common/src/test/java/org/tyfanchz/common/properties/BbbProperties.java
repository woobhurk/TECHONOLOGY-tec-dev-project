package org.tyfanchz.common.properties;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public enum BbbProperties implements TyzPropertiesParent {
    ABC("abc"),
    ACD("acd"),
    CHINESE("chinese")
    ;

    private final String propKey;

    BbbProperties(String propKey) {
        this.propKey = propKey;
    }

    @Override
    public String getPropKey() {
        return this.propKey;
    }
}
