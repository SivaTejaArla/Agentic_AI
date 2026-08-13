from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Greet the user first based on the current time of user and Answer user questions to the best of your knowledge',
)