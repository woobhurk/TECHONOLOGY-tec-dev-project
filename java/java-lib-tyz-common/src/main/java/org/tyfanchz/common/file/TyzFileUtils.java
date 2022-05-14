package org.tyfanchz.common.file;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * <p>Description: TyzFileUtils
 *
 * <p>文件操作工具类，提供如下操作</p>
 * <p>1. 遍历目录，获取所有项目</p>
 * <p>2. 遍历目录，仅获取文件夹</p>
 * <p>3. 遍历目录，仅获取文件</p>
 * <p>4. 遍历目录，通过指定的方式获取结果（是否递归、过滤、排序）</p>
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-20
 */
public class TyzFileUtils {
    private TyzFileUtils() {}

    public static List<Path> listAll(Path startPath, boolean needRecurse) {
        List<TyzFileOption> optionList = new ArrayList<>();

        optionList.add(TyzFileOption.LIST_ALL);
        optionList.add(TyzFileOption.SORT_ASC);

        if (needRecurse) {
            optionList.add(TyzFileOption.RECURSE);
        }

        return listItems(startPath, optionList.toArray(new TyzFileOption[0]));
    }

    public static List<Path> listDirectories(Path startPath, boolean needRecurse) {
        List<TyzFileOption> optionList = new ArrayList<>();

        optionList.add(TyzFileOption.LIST_DIR_ONLY);
        optionList.add(TyzFileOption.SORT_ASC);

        if (needRecurse) {
            optionList.add(TyzFileOption.RECURSE);
        }

        return listItems(startPath, optionList.toArray(new TyzFileOption[0]));
    }

    public static List<Path> listFiles(Path startPath, boolean needRecurse) {
        List<TyzFileOption> optionList = new ArrayList<>();

        optionList.add(TyzFileOption.LIST_FILE_ONLY);
        optionList.add(TyzFileOption.SORT_ASC);

        if (needRecurse) {
            optionList.add(TyzFileOption.RECURSE);
        }

        return listItems(startPath, optionList.toArray(new TyzFileOption[0]));
    }

    public static List<Path> listItems(Path startPath, boolean needRecurse) {
        Stream<Path> listedItemStream;
        List<Path> itemList = new ArrayList<>();

        if (Files.isRegularFile(startPath)) {
            itemList.add(startPath);
        } else {
            try {
                listedItemStream = needRecurse ? Files.walk(startPath) : Files.list(startPath);
                itemList.addAll(listedItemStream.collect(Collectors.toList()));
                itemList.sort(Path::compareTo);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return itemList;
    }

    public static List<Path> listItems(Path startPath, TyzFileOption... options) {
        TyzFileVisitor fileVisitor = new TyzFileVisitor(startPath, Arrays.asList(options));
        List<Path> itemList = new ArrayList<>();

        try {
            Files.walkFileTree(startPath, fileVisitor);
            itemList.addAll(fileVisitor.getItemList());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return itemList;
    }
}
