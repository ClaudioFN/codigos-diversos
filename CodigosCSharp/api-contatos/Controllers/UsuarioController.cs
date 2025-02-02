/*
Created Date: 21/10/2023
Last Update: 01/02/2025
Description: Class for to control users for the API
Observation: It contains details of date and time of the system and make a small presentation to the user showing the name
*/
using Microsoft.AspNetCore.Mvc;

namespace API_DIO.Controllers
{
    [ApiController]
    [Microsoft.AspNetCore.Components.Route("[controller]")]
    public class UsuarioController : ControllerBase
    {
        [HttpGet("ObterDataHoraAtual")]
        public IActionResult  ObterDataHora() 
        {
            var obj = new 
            {
                Data = DateTime.Now.ToLongDateString(),
                Hora = DateTime.Now.ToShortTimeString()
            };

            return Ok(obj);
        }

        [HttpGet("Apresentar/{nome}")]
        public IActionResult Apresentar(string nome) 
        {
            var mensagem = $"Olá {nome}, seja bem-vindo!";
            return Ok(new { mensagem });
        }
    }

}
