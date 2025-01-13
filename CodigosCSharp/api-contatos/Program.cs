/*
Created Date: 21/10/2023
Last Update: 12/01/2025
Description: Main class of the program
Observation: Concentrates the calling of the others methods by creating the database connection, controllers and endpoints
*/

using API_DIO.Context;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

/// TODO: TROCAR O UseSqlServer por MySql
builder.Services.AddDbContext<AgendaContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("ConexaoPadrao"))
);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
