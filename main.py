from agent.events import AgentEventType
from client.llm_client import LLMClient
import asyncio
import click
from typing import Any
from agent.agent import Agent
from ui.tui import TUI, get_console
import sys

console = get_console()
class CLI:
    def __init__(self):
        self.agent: Agent | None=None
        self.tui = TUI()

    async def run_single(self, message: str) -> str | None:
        async with Agent() as agent:
            self.agent = agent
            return await self._process_message(message)

    async def _process_message(self, message: str) -> str | None:
        if not self.agent:
            return None

        async for event in self.agent.run(message):
            if event.type == AgentEventType.TEXT_DELTA:
                content = event.data.get("content", "")
                self.tui.stream_asistent_delta(content)

@click.command()
@click.argument("prompt", required=False)
def main(prompt: str | None,):
    print(f"Hello from agent-code! {prompt}")
    cli = CLI()
    # messages = [{"role": "user", "content": prompt}]
    if prompt:
        result = asyncio.run(cli.run_single(prompt))
        if result is None:
            sys.exit(1)






main()
