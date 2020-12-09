package com.tyfanchz.java.stuspringbootaop.controller;

import java.util.HashMap;
import java.util.Map;
import com.tyfanchz.java.stuspringbootaop.annotation.EnableRequestLog;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <p>Description:
 * <p>Project: stu-spring-boot-aop
 *
 * @author wbh
 * @date 2020-12-07
 */
@RestController
@RequestMapping("/account")
public class AccountController {
    @EnableRequestLog
    @RequestMapping("/whoami")
    public String whoami() {
        return "/root";
    }

    @EnableRequestLog
    @RequestMapping("/test1")
    public Object test1(String name, String value) {
        Map<String, String> resp = new HashMap<>();
        resp.put("resp name", name);
        resp.put("resp value", value);

        return resp;
    }

    //@EnableRequestLog
    @RequestMapping("/test2")
    public Object test2(@RequestBody Map<String, String> req) throws Exception {
        Map<String, String> resp = new HashMap<>();
        req.forEach((key, value) -> resp.put("resp " + key, "resp " + value));

        throw new Exception("swifiwrevnier##^%&(&");
        //return resp;
    }
}
