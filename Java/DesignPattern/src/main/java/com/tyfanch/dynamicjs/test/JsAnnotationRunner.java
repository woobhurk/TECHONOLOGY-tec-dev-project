package com.tyfanch.dynamicjs.test;

import com.tyfanch.dynamicjs.annotation.ScriptMethod;
import com.tyfanch.dynamicjs.annotation.ScriptParam;
import com.tyfanch.dynamicjs.annotation.ScriptRunner;

@ScriptRunner
public interface JsAnnotationRunner {
    @ScriptMethod(script = "%1$s * %2$s;")
    double calMul(double a, double b);

    @ScriptMethod(script = "${a} / ${b}")
    double calDiv(@ScriptParam("a") double argA, @ScriptParam("b") double argB);

    @ScriptMethod(
        engine = "EMACScript",
        script = "var str = '%3$s: Yo${ no }u sho\\\\$uld use \\\\${a} to replace to ${ b  }'; print(str);")
    void formatStr(@ScriptParam("a") String argA, @ScriptParam("b") String argB, @ScriptParam("c") String argC);
}
