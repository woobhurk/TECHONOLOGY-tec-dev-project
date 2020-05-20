package org.tyfanchz.common.file;

import java.nio.file.FileVisitor;
import java.nio.file.Path;
import java.util.List;

/**
 * <p>Description: TyzBaseFileVisitor
 *
 * <p>文件遍历器基类</p>
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-20
 */
public abstract class TyzBaseFileVisitor implements FileVisitor<Path> {
    /**
     * 起始目录
     */
    protected Path startPath;
    /**
     * 遍历选项
     */
    protected List<TyzFileOption> optionList;

    protected TyzBaseFileVisitor(Path startPath,
        List<TyzFileOption> optionList) {
        this.startPath = startPath;
        this.optionList = optionList;
    }

    /**
     * 获取最终遍历得到的结果，根据 {@link #optionList} 的得到结果。
     *
     * @return 遍历结果
     */
    public abstract List<Path> getItemList();
}
