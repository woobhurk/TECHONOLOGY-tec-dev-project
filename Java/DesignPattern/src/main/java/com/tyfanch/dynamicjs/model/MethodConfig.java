package com.tyfanch.dynamicjs.model;

import java.io.Serializable;

public class MethodConfig implements Serializable {
    private String engine;
    private String script;

    public String getEngine() {
        return this.engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }

    public String getScript() {
        return this.script;
    }

    public void setScript(String script) {
        this.script = script;
    }

    @Override
    public String toString() {
        return "MethodConfig{" +
            "engine='" + this.engine + '\'' +
            ", script='" + this.script + '\'' +
            '}';
    }
}
