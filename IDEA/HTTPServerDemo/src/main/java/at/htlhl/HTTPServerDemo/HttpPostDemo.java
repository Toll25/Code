package at.htlhl.HTTPServerDemo;

import at.htlhl.HTTPServerDemo.model.Product;
import jdk.jfr.ContentType;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HttpPostDemo {
    public static final String POST_REQUEST_URL = "https://fruitshop2-predic8.azurewebsites.net/shop/v2/products";

    public HttpPostDemo() throws RuntimeException {
        String json = """
                {
                  "name": "Linuxbeere",
                  "price": 69.69
                }
                """;
        System.out.println(json);
        try {
            HttpRequest request = HttpRequest.newBuilder(new URI(POST_REQUEST_URL))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(json))
                    .build();
            HttpClient httpClient = HttpClient.newHttpClient();
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            if(response.statusCode()== HttpURLConnection.HTTP_CREATED){
                System.out.println(response);
            }
        } catch (URISyntaxException | IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new HttpPostDemo();
    }

}
