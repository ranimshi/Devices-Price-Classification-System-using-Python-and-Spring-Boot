package com.example.spring.boot.AP.controller;

import com.example.spring.boot.AP.model.DeviceSpecs;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/api")
public class PricePredictionController {

    // Define the endpoint for predicting the price of a device
    @PostMapping("/predict")
    public String predictPrice(@RequestBody DeviceSpecs deviceSpecs) {
        // Call the Python model function to predict the price range
        String predictedPriceRange = callPythonModel(deviceSpecs);
        
        // Return the predicted price range
        return predictedPriceRange;
    }

    // Define the method to call the Python model function
    private String callPythonModel(DeviceSpecs deviceSpecs) {
        // Define the URL of the Python model endpoint
        String pythonModelUrl = "http://localhost:5000/predict";
        
        // Create a RestTemplate object for making HTTP requests
        RestTemplate restTemplate = new RestTemplate();
        
        // Make a POST request to the Python model endpoint
        ResponseEntity<String> response = restTemplate.postForEntity(pythonModelUrl, deviceSpecs, String.class);
        
        // Return the response body (predicted price range)
        return response.getBody();
    }
}
