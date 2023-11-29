package at.htlhl.HTTPServerDemo;

import at.htlhl.HTTPServerDemo.model.Product;
import at.htlhl.HTTPServerDemo.model.Products;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.json.JsonMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Iterator;

/**
 * Demonstriert wie ein GET-Request abgesetzt wird
 *
 * @author baul
 */
public class HTTPClientDemo {

    private ObjectMapper jsonMapper = new ObjectMapper();
    /**
     * Defines the REST-Endpoint URL
     */
    public static final String endPoint = "https://api.predic8.de/shop/v2/products";

    public HTTPClientDemo() {
        /**
         * HTTP GET-Request erzeugen
         */
        try {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(new URI(endPoint))
                    .GET()
                    .build();
            HttpClient httpClient = HttpClient.newHttpClient();
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Status code: " + response.statusCode());
            if (response.statusCode() == HttpURLConnection.HTTP_OK) {
                final JsonNode node = jsonMapper.readTree(response.body());
                if (node.has("products")) {
                    JsonNode products = node.get("products");

                    if (products.isArray()) {
                        ArrayNode arrayNode = (ArrayNode) products;
                        Iterator<JsonNode> iter = arrayNode.elements();

                        while (iter.hasNext()) {
                            JsonNode productNode = iter.next();
                            if (productNode.has("self_link")) {
                                System.out.println("self_link: " + productNode.get("self_link"));
                            }
                        }
                    }
                }
                //System.out.println("Body:\n" + response.body());
            }


        } catch (URISyntaxException ex) {
            System.err.println("URISyntaxException: " + ex.getMessage());
            System.err.println("Program will end");
            System.exit(1);
        } catch (IOException ex) {
            System.err.println("IOException: " + ex.getMessage());
            System.err.println("Program will end");
            System.exit(1);
        } catch (InterruptedException ex) {
            System.err.println("InterruptedException: " + ex.getMessage());
            System.err.println("Program will end");
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        new HTTPClientDemo();
    }
}