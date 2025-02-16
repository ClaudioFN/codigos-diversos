/*
Created Date: 21/10/2023
Last Update: 16/02/2025
Description: Class with the definition o Contato
Observation: Entity class for Contato
*/

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