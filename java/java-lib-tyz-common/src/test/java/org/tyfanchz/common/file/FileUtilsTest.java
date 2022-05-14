package org.tyfanchz.common.file;

import java.nio.file.Paths;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-20
 */
public class FileUtilsTest {
    public static void main(String[] args) {
        //testFileUtils();
        testFileUtils2();
    }

    private static void testFileUtils() {
        TyzFileUtils.listItems(Paths.get("D:/__WORK__"), true)
            .forEach(System.out::println);

        System.out.println("*************************");

        TyzFileUtils.listItems(Paths.get("D:/__WORK__"), false)
            .forEach(System.out::println);
    }

    private static void testFileUtils2() {
        TyzFileUtils.listDirectories(Paths.get("D:/__WORK__"), true)
            .forEach(System.out::println);

        System.out.println("*************************");

        TyzFileUtils.listItems(Paths.get(
            "D:/__WORK__/__glsx__"), TyzFileOption.LIST_ALL, TyzFileOption.EXCLUDE_START_PATH)
            .forEach(System.out::println);
    }
}
