package org.tyfanchz.common.properties;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-19
 */
public class PropertiesUtilsTest {
    public static void main(String[] args) {
        test();
    }

    private static void test() {
        TyzPropertiesUtils.loadConfig(PropertiesConfig.class);
        System.out.println(AaaProperties.PROP_TEST.get());
        System.out.println(BbbProperties.ABC.get());
        System.out.println(BbbProperties.ACD.get());
        System.out.println(BbbProperties.CHINESE.get());
    }
}
