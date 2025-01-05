/*
Created Date: 31/07/2022
Last Update: 04/01/2025
Description: Creating a web crawler to search throw a specific website
Observation: Only one class gere StartWebCrawler
*/
import java.util.logging.Logger;

public class StartWebCrawler {
    private static final Logger LOGGER = Logger.getLogger(WebCrawler.class.getName());
    public static void main(String[] args) {
        WebCrawler crawler = new WebCrawler();
        LOGGER.info("Nome da classe a ser registrada no LOG: " + LOGGER.getName());
        String raizURL = "https://www.gov.br/pt-br/servicos/obter-passaporte-comum-para-brasileiro";
        LOGGER.info("URL Raiz: " + raizURL);
        crawler.crawl(raizURL, 100);
    }
}
