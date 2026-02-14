from client.llm_client import LLMClient
import asyncio

async def main():
    print("Hello from agent-code!")
    client = LLMClient()
    messages = [{"role": "user", "content": "What's up"}]
    async for event in client.chat_completion(messages, True):
        print(event)



asyncio.run(main())
