package org.tyfanchz.common.file;

import java.io.File;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * <p>Description: TyzFileVisitor
 *
 * <p>文件遍历器</p>
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-20
 */
public class TyzFileVisitor extends TyzBaseFileVisitor {
    private final List<Path> mixedItemList = new ArrayList<>();
    private final List<Path> directoryList = new ArrayList<>();
    private final List<Path> fileList = new ArrayList<>();

    protected TyzFileVisitor(Path startPath, List<TyzFileOption> optionList) {
        super(startPath, optionList);
    }

    @Override
    public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
        throws IOException {

        FileVisitResult visitResult;
        Path processedDir;

        // 判断是否剔除起始目录，
        // 如果不包含 EXCLUDE_START_PATH 选项或当前目录不为起始目录则需要添加到列表中
        if (!super.optionList.contains(TyzFileOption.EXCLUDE_START_PATH)
            || dir.compareTo(this.startPath) != 0) {
            // 判断是否加上路径分隔符
            processedDir = super.optionList.contains(TyzFileOption.ADD_DIR_TAIL)
                ? Paths.get(dir.toString() + File.separator)
                : dir;
            this.mixedItemList.add(processedDir);
            this.directoryList.add(processedDir);
        }

        // 判断是否需要继续遍历子项目
        if (dir.compareTo(this.startPath) == 0
            || super.optionList.contains(TyzFileOption.RECURSE)) {
            // 如果当前目录是起始目录，或者需要递归，则继续遍历
            visitResult = FileVisitResult.CONTINUE;
        } else {
            visitResult = FileVisitResult.SKIP_SUBTREE;
        }

        return visitResult;
    }

    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
        FileVisitResult visitResult;

        this.mixedItemList.add(file);
        this.fileList.add(file);

        visitResult = FileVisitResult.CONTINUE;

        return visitResult;
    }

    @Override
    public FileVisitResult visitFileFailed(Path file, IOException exc) throws IOException {
        return FileVisitResult.CONTINUE;
    }

    @Override
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
        return FileVisitResult.CONTINUE;
    }

    @Override
    public List<Path> getItemList() {
        List<Path> itemList;

        // 判断返回哪些项目
        if (super.optionList.contains(TyzFileOption.LIST_DIR_ONLY)
            || super.optionList.contains(TyzFileOption.LIST_FILE_ONLY)) {
            // 仅仅返回目录或文件列表
            itemList = this.getSpecifiedItemList();
        } else {
            // 如果都没指定，则返回所有
            itemList = this.getAllItemList();
        }

        return itemList;
    }

    /**
     * 返回所有遍历项目，通过 {@link TyzFileOption#LIST_ALL} 指定。
     *
     * @return 所有遍历出来的项目
     */
    private List<Path> getAllItemList() {
        List<Path> allItemList = new ArrayList<>();

        if (super.optionList.contains(TyzFileOption.ORDER_DIR_FIRST)) {
            // 文件夹优先
            allItemList.addAll(this.getSortedItemList(this.directoryList));
            allItemList.addAll(this.getSortedItemList(this.fileList));
        } else if (super.optionList.contains(TyzFileOption.ORDER_FILE_FIRST)) {
            // 文件优先
            allItemList.addAll(this.getSortedItemList(this.fileList));
            allItemList.addAll(this.getSortedItemList(this.directoryList));
        } else {
            // 混合
            allItemList.addAll(this.getSortedItemList(this.mixedItemList));
        }

        return allItemList;
    }

    /**
     * 返回指定的项目，通过 {@link TyzFileOption#LIST_DIR_ONLY}
     * 或 {@link TyzFileOption#LIST_FILE_ONLY} 指定。
     *
     * @return 遍历出来的指定项目
     */
    private List<Path> getSpecifiedItemList() {
        List<Path> specifiedItemList;

        if (super.optionList.contains(TyzFileOption.LIST_DIR_ONLY)) {
            // 仅仅返回目录列表
            specifiedItemList = this.getSortedItemList(this.directoryList);
        } else {
            // 仅仅返回文件列表
            specifiedItemList = this.getSortedItemList(this.fileList);
        }

        return specifiedItemList;
    }

    private List<Path> getSortedItemList(List<Path> itemList) {
        List<Path> sortedItemList;

        if (this.optionList.contains(TyzFileOption.SORT_ASC)) {
            sortedItemList = this.sortItemAsc(itemList);
        } else if (this.optionList.contains(TyzFileOption.SORT_DESC)) {
            sortedItemList = this.sortItemDesc(itemList);
        } else {
            sortedItemList = itemList;
        }

        return sortedItemList;
    }

    private List<Path> sortItemAsc(List<Path> itemList) {
        itemList.sort(Comparator.naturalOrder());

        return itemList;
    }

    private List<Path> sortItemDesc(List<Path> itemList) {
        itemList.sort(Comparator.reverseOrder());

        return itemList;
    }
}
