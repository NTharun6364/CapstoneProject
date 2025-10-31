package com.example.utils;

import com.opencsv.CSVReader;
import java.io.FileReader;
import java.util.*;

public class ExcelUtils {
    // Simple CSV reader that returns list of maps (header -> value)
    public static List<Map<String, String>> loadData(String csvPath) throws Exception {
        List<Map<String, String>> rows = new ArrayList<>();
        try (CSVReader reader = new CSVReader(new FileReader(csvPath))) {
            String[] headers = reader.readNext();
            if (headers == null) return rows;
            String[] line;
            while ((line = reader.readNext()) != null) {
                Map<String, String> map = new HashMap<>();
                for (int i = 0; i < headers.length && i < line.length; i++) {
                    map.put(headers[i].trim(), line[i].trim());
                }
                rows.add(map);
            }
        }
        return rows;
    }
}
