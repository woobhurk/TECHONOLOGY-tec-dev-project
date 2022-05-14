package org.tyfanchz.common.datetime;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author wbh
 * @date 2020-05-19
 */
public class DateTimeUtilsTest {
    public static void main(String[] args) {
        testDateTimeUtils();
    }

    private static void testDateTimeUtils() {
        System.out.println(TyzDateTimeUtils.formatNow());
        System.out.println(TyzDateTimeUtils.format(345689606L));
        System.out.println(TyzDateTimeUtils.addDay("2020-03-04 12:33:44", 200));
        System.out.println(TyzDateTimeUtils.format(TyzDateTimeUtils.addDay("2020-03-04 12:33:44", -200)));
    }
}
