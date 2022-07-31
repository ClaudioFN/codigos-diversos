import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

// Logs
import java.util.logging.Level;
import java.util.logging.Logger;

public class WebCrawler {

    private Queue<String> filaDeUrls;
    private List<String> urlVisitadas;
    private String diaHora = new SimpleDateFormat("ddMMyyyyHHmmss").format(Calendar.getInstance().getTime());
    private String nomeArquivo = "ListaDeURLs_"+ diaHora +".txt";
    PrintWriter writer;
    // LOG
    private static final Logger LOGGER = Logger.getLogger(WebCrawler.class.getName());

    /* Construtor - WebCrawler
     * Criar os objetos / Alocar memoria para as variaveis
    */
    public WebCrawler() {
        try{
            writer = new PrintWriter(nomeArquivo);
        }catch(Exception e){
            LOGGER.log(Level.SEVERE, "Exception 1", e);
            e.printStackTrace();
        }
        filaDeUrls = new LinkedList<>();
        urlVisitadas = new ArrayList<>();


    }

    /* Metodo - crawl 
    * Avancar para dentro da lista de URL disponiveis a partir de uma raiz. Chamado pelo metodo main.
    * String raizURL - ponto(URL) de partida
    * int breakpoint - limite de URLs a serem buscadas
    */ 
    public void crawl(String raizURL, int breakpoint) {
        String nomeMetodo = new Object(){}.getClass().getEnclosingMethod().getName();
        LOGGER.info("Metodo em execucao: " + nomeMetodo);

        LOGGER.info("Parametros de entrada: raizURL " + raizURL + ", breakpoint: " + breakpoint);
        filaDeUrls.add(raizURL);
        urlVisitadas.add(raizURL);
        
        LOGGER.info("Antes do loop");
        while(!filaDeUrls.isEmpty()){

            String s = filaDeUrls.remove();
            String HtmlPuro = "";
            LOGGER.info("URL atual: " + s);
            try{
                // Criar URL com a string fornecida e removida da fila anteriormente
                URL url = new URL(s);
                BufferedReader entra = new BufferedReader(new InputStreamReader(url.openStream()));
                String linhaDeEntrada = entra.readLine();
                
                // Ler todas a linhas do conteudo da URL
                // e concatenar cada linha no HtmlPuro ate que todas as linhas sejam lidas
                while(linhaDeEntrada  != null){
                    HtmlPuro += linhaDeEntrada;
                    linhaDeEntrada = entra.readLine();
                }
                // Fecha o buffer aberto
                entra.close();
            } catch (Exception e){
                LOGGER.log(Level.SEVERE, "Exception 2", e);
                e.printStackTrace();
                writer.close();
            }
             
            // REGEX compativel com a URL
            // para validar o HTML na busca da URL
            String padraoValidoURL = "(www|http:|https:)+[^\s]+[\\w]";
            Pattern padrao = Pattern.compile(padraoValidoURL);
            Matcher compativel = padrao.matcher(HtmlPuro);
            
            // A cada vez que o REGEX da URL for compativel com o HTML
            // adiconar ela a lista da fila de proxima URL a ser acessada e marcada como visitada
            try{
                breakpoint = getBreakpoint(breakpoint, compativel);
            }catch(Exception e){
                LOGGER.log(Level.SEVERE, "Exception 3", e);
                e.printStackTrace();
                writer.close();
            }            
    
            // Sair do loop mais externo se ele atingir o ponto de interrup��o
            if(breakpoint == 0){
                break;
            }
        }

    }

    /* Metodo - getBreakpoint
     * Encontrar URLs validas na lista de HtmlPuro
     * int breakpoint - numero inteiro que e decrementado a cada execucao ate o limite 0
     * Matcher compativel - valor compativel com o tipo de URL buscada
     */
    private int getBreakpoint(int breakpoint, Matcher compativel) {
        String nomeMetodo = new Object(){}.getClass().getEnclosingMethod().getName();
        LOGGER.info("Metodo em execucao: " + nomeMetodo);

        while(compativel.find()){
            String URLatual = compativel.group();
            // Caso nao tenha a URL, adiciona na lista, exibe e depois salva na lista de URLs visitadas
            if(!urlVisitadas.contains(URLatual)){
                urlVisitadas.add(URLatual);
                // Escrever no arquivo as URLs encontradas
                writer.write("\nSite encontrato com uma URL valida: " + URLatual);
                filaDeUrls.add(URLatual);
            }
    
            // Sair do loop quando chegar a 0
            if(breakpoint == 0){
                break;
            }
            // Trata de chegar no limite definido para busca de URLs
            breakpoint--;
        }
        return breakpoint;
    }


}