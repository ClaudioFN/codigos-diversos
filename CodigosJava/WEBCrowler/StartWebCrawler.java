
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
