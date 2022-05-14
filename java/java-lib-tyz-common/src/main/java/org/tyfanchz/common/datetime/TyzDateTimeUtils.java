package org.tyfanchz.common.datetime;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * <p>Description: TyzDateTimeUtils
 *
 * <p>时间格式化工具类</p>
 *
 * <p>Project: tyz-common
 *
 * @author wbh
 * @date 2020-05-19
 */
public class TyzDateTimeUtils {
    private TyzDateTimeUtils() {}

    /**
     * 日期格式，如 {@code 2020-01-01}
     */
    public static final String PATTERN_DATE = "yyyy-MM-dd";

    /**
     * 时间格式，如 {@code 11:03:00}
     */
    public static final String PATTERN_TIME = "HH:mm:ss";

    /**
     * 时间+日期格式，如 {@code 2020-01-01 11:03:00}
     */
    public static final String PATTERN_DATE_TIME = PATTERN_DATE + " " + PATTERN_TIME;

    /**
     * @see #PATTERN_DATE_TIME
     */
    public static final String PATTERN_ISO = PATTERN_DATE_TIME;

    /**
     * 一分钟的秒数
     */
    public static final long SECONDS_PER_MINUTE = 60;

    /**
     * 一小时的秒数
     */
    public static final long SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60;

    /**
     * 一天的秒数
     */
    public static final long SECONDS_PER_DAY = SECONDS_PER_HOUR * 24;

    /**
     * 一周的秒数
     */
    public static final long SECONDS_PER_WEEK = SECONDS_PER_DAY * 7;

    /**
     * 一个月（30天）的秒数
     */
    public static final long SECONDS_PER_MONTH = SECONDS_PER_DAY * 30;

    /**
     * 一年（365天）的秒数
     */
    public static final long SECONDS_PER_YEAR = SECONDS_PER_DAY * 365;

    /**
     * 格式化当前时间，格式为默认ISO格式：{@link #PATTERN_ISO}
     *
     * @return 格式化后的当前时间
     */
    public static String formatNow() {
        return format(new Date());
    }

    /**
     * 指定毫秒数格式化时间
     *
     * @param milliseconds 毫秒数
     * @return 格式化后的时间
     */
    public static String format(long milliseconds) {
        return format(new Date(milliseconds));
    }

    /**
     * 指定日期对象格式化时间
     *
     * @param dateTime 日期对象
     * @return 格式化后的时间
     */
    public static String format(Date dateTime) {
        SimpleDateFormat sdf = new SimpleDateFormat(PATTERN_ISO);
        String dateTimeStr;

        dateTimeStr = sdf.format(dateTime);

        return dateTimeStr;
    }

    public static Date parse(String dateTimeStr) {
        return parse(dateTimeStr, PATTERN_ISO);
    }

    public static Date parse(String dateTimeStr, String pattern) {
        SimpleDateFormat sdf = new SimpleDateFormat(pattern);
        Date dateTime;

        try {
            dateTime = sdf.parse(dateTimeStr);
        } catch (ParseException e) {
            dateTime = null;
        }

        return dateTime;
    }

    public static Date addYear(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.YEAR, amount);
    }

    public static Date addMonth(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.MONTH, amount);
    }

    public static Date addDay(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.DAY_OF_MONTH, amount);
    }

    public static Date addHour(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.HOUR_OF_DAY, amount);
    }

    public static Date addMinute(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.MINUTE, amount);
    }

    public static Date addSecond(String dateTimeStr, int amount) {
        return addField(dateTimeStr, Calendar.SECOND, amount);
    }

    public static Date addField(String dateTimeStr, int field, int amount) {
        return addField(parse(dateTimeStr), field, amount);
    }

    public static Date addYear(Date dateTime, int amount) {
        return addField(dateTime, Calendar.YEAR, amount);
    }

    public static Date addMonth(Date dateTime, int amount) {
        return addField(dateTime, Calendar.MONTH, amount);
    }

    public static Date addDay(Date dateTime, int amount) {
        return addField(dateTime, Calendar.DAY_OF_MONTH, amount);
    }

    public static Date addHour(Date dateTime, int amount) {
        return addField(dateTime, Calendar.HOUR_OF_DAY, amount);
    }

    public static Date addMinute(Date dateTime, int amount) {
        return addField(dateTime, Calendar.MINUTE, amount);
    }

    public static Date addSecond(Date dateTime, int amount) {
        return addField(dateTime, Calendar.SECOND, amount);
    }

    public static Date addField(Date dateTime, int field, int amount) {
        Calendar calendar = Calendar.getInstance();

        calendar.setTime(dateTime);
        calendar.add(field, amount);

        return calendar.getTime();
    }
}
