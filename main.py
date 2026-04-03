import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from google.adk.agents import SequentialAgent
from vertexai.preview.reasoning_engines import AdkApp

from agents.research_loop import research_loop
from agents.security import security_agent
from agents.reporting import reporting_agent

root_agent = SequentialAgent(
    name='SecurityLead',
    sub_agents=[
        research_loop,
        security_agent,
        reporting_agent
    ]
)

app = AdkApp(agent=root_agent)

if __name__ == "__main__":
    pass
