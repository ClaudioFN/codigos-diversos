/*
Created Date: 21/10/2023
Last Update: 19/01/2025
Description: Class for items to add new contacts
Observation: Add context to the of contacts 
*/
using API_DIO.Entities;
using Microsoft.EntityFrameworkCore;

namespace API_DIO.Context
{
    public class AgendaContext : DbContext
    {
        public AgendaContext(DbContextOptions<AgendaContext> options) :base(options)
        {

        }

        public DbSet<Contato> Contatos { get; set; }
    }
}
