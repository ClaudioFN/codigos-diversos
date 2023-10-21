namespace API_DIO.Entities
{
    public class Contato
    {
        public int Id { get; set; }
        public string Nome { get; set; }
        public string Telefone { get; set; }
        public bool Ativo { get; set; }
    }
}

/// TODO: COMANDOS
/// Aplicar Migration: dotnet-ef database update
/// Executar o projeto API: dotnet watch run