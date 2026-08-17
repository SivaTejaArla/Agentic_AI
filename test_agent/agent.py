from google.adk.agents.llm_agent import Agent


from datetime import datetime



def getCurrentTime():

    currentTime = datetime.now()

    return currentTime
def convertToDays(age: int) -> int:
    return age*365

root_agent = Agent(
    model="gemini-flash-latest",  ## Name of the model being used 
    name="root_agent",              ## Name of the agent 
    description="A helpful assistant for user questions.", ## Description about the agent 
    instruction="""            
    Always start the very first response with a warm greeting based on getCurrentTime.
    Then ask the user for their name.
    After that,ask about their age. Convert to days using convertToDays

    """, ## Instructions to the agent like how to start the conversation

    tools=[getCurrentTime,convertToDays] ## External tools that can be used by the agent to process
)

print("Agent Created Successfully!!")