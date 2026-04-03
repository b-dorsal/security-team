from google.adk.agents import LlmAgent
from tools.cloud_tools import query_cloud_config, list_available_resources

data_collection_agent = LlmAgent(
  name='DataCollectionAgent',
  model='gemini-2.5-flash',
  description=(
      'Collect cloud configuration information related to the given topic area.'
  ),
  instruction="""You are an expert at reading cloud configuration JSON data and retrieving it. 
  
  Your responsibilities:
  1. Use the `list_available_resources` tool to see all available cloud config resource names
  2. Look at the conversation history to see what resource type you should collect:
     - First iteration: collect based on the initial user request
     - Subsequent iterations: look for "<NEXT_RESOURCE>[resource_type]</NEXT_RESOURCE>" in the MisconfigurationAgent's previous response
  3. Pick the resource name that most closely matches what you need to gather
  4. Use the `query_cloud_config` tool to retrieve all resources of that type
  5. Be concise and just collect the data - the MisconfigurationAgent will analyze it""",
  tools=[query_cloud_config, list_available_resources]
)
