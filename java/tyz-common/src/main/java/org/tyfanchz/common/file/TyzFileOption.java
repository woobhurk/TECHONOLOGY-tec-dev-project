package org.tyfanchz.common.file;

/**
 * <p>Description: TyzFileOption
 *
 * <p>文件遍历选项</p>
 *
 * <p>Project: tyz-common
 *
 * @author tyfanchz
 * @date 2020-05-20
 */
public enum TyzFileOption {
    /**
     * 递归遍历
     */
    RECURSE,
    /**
     * 列出全部（默认）
     */
    LIST_ALL,
    /**
     * 仅列出目录
     */
    LIST_DIR_ONLY,
    /**
     * 仅列出文件
     */
    LIST_FILE_ONLY,
    /**
     * 目录和文件混合（默认）
     */
    ORDER_MIXED,
    /**
     * 目录优先
     */
    ORDER_DIR_FIRST,
    /**
     * 文件优先
     */
    ORDER_FILE_FIRST,
    /**
     * 正序排序
     */
    SORT_ASC,
    /**
     * 倒序排序
     */
    SORT_DESC,
    /**
     * 给目录项加上路径分隔符后缀
     */
    ADD_DIR_TAIL,
    /**
     * 结果里面不包含起始目录
     */
    EXCLUDE_START_PATH,
}
