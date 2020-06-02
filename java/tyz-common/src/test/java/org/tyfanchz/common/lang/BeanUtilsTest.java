package org.tyfanchz.common.lang;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author wbh
 * @date 2020-06-02
 */
public class BeanUtilsTest {
    public static void main(String[] args) {
        testCopyProperties();
    }

    private static void testCopyProperties() {
        TestSrc testSrc = new TestSrc();
        TestTarget testTarget = new TestTarget();
        System.out.println(TyzBeanUtils.copyProperties(testSrc, testTarget));
    }
}
