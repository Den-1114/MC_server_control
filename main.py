import typer as ty
import os
from colorama import Fore
from time import sleep

app = ty.Typer()

@app.command()
def start():
    ty.secho(""" __  __ _                            __ _                                  
|  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_   ___  ___ _ ____   _____ _ __ 
| |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| / __|/ _ \ '__\ \ / / _ \ '__|
| |  | | | | | |  __/ (__| | | (_| |  _| |_  \__ \  __/ |   \ V /  __/ |   
|_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__| |___/\___|_|    \_/ \___|_|   
  ___ ___  _ __ | |_ _ __ ___ | |                                          
 / __/ _ \| '_ \| __| '__/ _ \| |                                          
| (_| (_) | | | | |_| | | (_) | |                                          
 \___\___/|_| |_|\__|_|  \___/|_|                                          """, fg="yellow")
    if os.path.exists("server.jar"):
        ty.echo("   ")
        ty.echo("   ")
        ty.secho("Server found!", fg="green")
        ty.echo("   ")
        ty.echo("   ")
        try:
            sa =int(input(f"{Fore.BLUE}How many MB RAM do you want the server to use? (Example: 4096) : "))
        except ValueError:
            ty.secho("Invalid input!", fg="red")
            ty.secho("Setting the RAM to 4096 MB", fg="green")
            sleep(5)
            sa = 4096
        
        ty.echo("   ")
        ty.echo("   ")
        sr = input(f"{Fore.BLUE}Do you want the server to hava a pretty control panel? (y/n) : ")
        ty.echo("   ")
        ty.echo("   ")
        ty.secho(f"Starting server...{Fore.YELLOW}", fg="green")
        ty.echo("   ")
        ty.echo("   ")
        if sr == "y":
            os.system(f"java -Xmx{str(sa)}M -Xms{str(sa)}M -jar server.jar")
        else:
            os.system(f"java -Xmx{str(sa)}M -Xms{str(sa)}M -jar server.jar nogui")
        ty.secho("The server stoped!", fg="red")
    else:
        ty.secho("Server not found!", fg="red")


    
    




if __name__ == "__main__":
    app()
