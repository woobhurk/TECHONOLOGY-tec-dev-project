package org.tyfanchz.common.lang;

import java.lang.reflect.Field;

/**
 * <p>Description:
 *
 * <p>Project: tyz-common
 *
 * @author wbh
 * @date 2020-06-02
 */
public class TyzBeanUtils {
    private TyzBeanUtils() {}

    public static <S, T> T copyProperties(S src, T target) {
        Class<?> srcClass = src.getClass();
        Class<?> targetClass = target.getClass();
        Field[] srcFields = srcClass.getDeclaredFields();

        for (Field srcField : srcFields) {
            try {
                String name = srcField.getName();
                Field targetField = targetClass.getDeclaredField(name);

                if (targetField.getType().isAssignableFrom(srcField.getType())) {
                    srcField.setAccessible(true);
                    targetField.setAccessible(true);
                    targetField.set(target, srcField.get(src));
                }
            } catch (NoSuchFieldException e) {
                System.out.println(targetClass.getName() + " has no field named "
                    + srcField.getName());
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        }

        return target;
    }
}
