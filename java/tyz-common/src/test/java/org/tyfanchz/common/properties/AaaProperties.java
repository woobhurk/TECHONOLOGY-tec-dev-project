package org.tyfanchz.common.properties;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public enum AaaProperties implements TyzPropertiesParent {
    PROP_TEST("propTest"),
    ;

    private final String propKey;

    AaaProperties(String propKey) {
        this.propKey = propKey;
    }

    @Override
    public String getPropKey() {
        return this.propKey;
    }
}
