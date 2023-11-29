package at.htlhl.HTTPServerDemo.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.JsonNode;

import java.util.List;

public class Product {
    private int id;
    private String name;
    @JsonProperty("self_link")
    private String productURL;

    public Product(){

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getProductURL() {
        return productURL;
    }

    public void setProductURL(String productURL) {
        this.productURL = productURL;
    }

    @Override
    public String toString() {
        return "Product:" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", productURL='" + productURL;
    }
}
