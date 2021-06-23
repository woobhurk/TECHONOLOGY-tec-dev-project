package com.tyfanchz.sscd01gateway.modules.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <p>Description:
 * <p>Project: stu-spring-cloud-demo01
 *
 * @author wbh
 * @date 2021-06-22
 */
@RestController
@RequestMapping("/consul")
@Slf4j
public class HealthController {
    @GetMapping("/checkHealth")
    public String checkHealth() {
        return "OK";
    }
}
