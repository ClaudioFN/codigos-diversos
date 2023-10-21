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
