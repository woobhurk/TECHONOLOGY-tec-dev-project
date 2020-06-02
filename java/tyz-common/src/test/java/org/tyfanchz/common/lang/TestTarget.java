package org.tyfanchz.common.lang;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author wbh
 * @date 2020-06-02
 */
public class TestTarget {
    private String name;
    private Integer age;
    private Integer day;

    @Override
    public String toString() {
        return "TestTarget{" +
            "name='" + this.name + '\'' +
            ", age=" + this.age +
            ", day=" + this.day +
            '}';
    }
}
