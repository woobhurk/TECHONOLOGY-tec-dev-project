package com.tyfanch.dynamicjs.test;

import com.tyfanch.dynamicjs.annotation.ScriptMethod;
import com.tyfanch.dynamicjs.annotation.ScriptParam;
import com.tyfanch.dynamicjs.annotation.ScriptRunner;

@ScriptRunner
public interface JsAnnotationRunner {
    @ScriptMethod(script = "%1$s * %2$s;")
    Double calMul(double a, double b);

    @ScriptMethod(script = "${a} / ${b}")
    Double calDiv(@ScriptParam("a") double argA, @ScriptParam("b") double argB);

    @ScriptMethod(
        engine = "EMACScript",
        scripts = {
            "var str = '%3$s: Yo${ no }u sho\\\\$uld use \\\\${a} to replace to ${ b  }'",
            "print(str);",
            "print('${b} !== ${a}');",
            "for (var i = 0; i < 100; i++) {",
            "    print('${c} current i = ' + i)",
            "}"
        })
    void formatStr(@ScriptParam("a") String argA, @ScriptParam("b") String argB, @ScriptParam("c") String argC);
}
