package at.htlhl.weatherserver.controllers;

import io.swagger.v3.oas.annotations.Operation;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.sql.PreparedStatement;

@RestController
@RequestMapping("/weatherServer/greetings")
public class GreetingController {

    private static final String HELLO_RESPONSE = """
            {
               "type": "greeting",
               "value": "hello ${name}"
            }   
            """;

    @GetMapping(value = "/hello", produces = "application/json")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "say hello to the given name")
    public String sayHello(@RequestParam(defaultValue = "World") String name) {
        return HELLO_RESPONSE.replace("${name}", name);
    }

    /***
     * alternative implementation of sayHello
     * @return
     */
    @GetMapping(value = "/hello/{name}", produces = "application/json")
    @Operation(summary = "say hello to name")
    @ResponseStatus(HttpStatus.OK)
    public String sayHelloAlternative(@PathVariable String name) {
        return HELLO_RESPONSE.replace("${name}", name);
    }
}
