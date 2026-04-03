import re
from typing import AsyncGenerator
from google.adk.agents import BaseAgent, LoopAgent
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext
from .data_collection import data_collection_agent
from .misconfiguration import misconfiguration_agent

class CheckStatusAndEscalate(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        events = ctx.session.events
        should_stop = False
        
        # Search backwards starting from the most recent MisconfigurationAgent event
        # This prevents accidental matches on older messages
        for event in reversed(events):
            # Only process if from the misconfiguration agent
            if getattr(event, 'author', '') == 'MisconfigurationAgent' and hasattr(event, 'content') and event.content:
                content_str = str(event.content)
                
                # Look for the exact <NEXT_RESOURCE> tag format
                match = re.search(r'<NEXT_RESOURCE>(.*?)</NEXT_RESOURCE>', content_str, re.DOTALL)
                if match:
                    resource_type = match.group(1).strip()
                    if resource_type.upper() == "STOP":
                        should_stop = True
                
                # After we've found the most recent event from MisconfigurationAgent, check it and then stop further searching
                break
        
        # Escalate to gracefully exit the loop and return results to parent agent
        yield Event(author=self.name, actions=EventActions(escalate=should_stop))

research_loop = LoopAgent(
  name='ResearchLoop',
  max_iterations=10,
  sub_agents=[data_collection_agent, misconfiguration_agent, CheckStatusAndEscalate(name="StopChecker")], 
)
