from util import *

app = get_app()
agents = get_agents()
while True:
    app(agents, input(f"\nEnter llm request: "))
    