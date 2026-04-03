from google.adk.agents import LlmAgent
from tools.cloud_tools import list_available_resources

misconfiguration_agent = LlmAgent(
  name='MisconfigurationAgent',
  model='gemini-2.5-pro',
  description=(
      'Review cloud configuration data identify any misconfigurations that could lead to security concerns.'
  ),
  instruction="""You are a cloud security expert specialized in identifying security misconfigurations.

  Your responsibilities:
  1. Review the cloud configuration data that was just collected by DataCollectionAgent
  2. Identify specific misconfigurations that could lead to security concerns
  3. For each finding, note which resource has the issue and what the specific problem is
  4. Be concise - provide findings in a structured format like "Resource: [resource_id], Issue: [brief description]"
  5. After reporting findings, decide if you need more data from related resources
  
  CRITICAL: If examining compute instances, you MUST sequentially request to review related resources. You should look for:
  - firewall_rules
  - service_accounts
  - iam_bindings (or iam_policies)
  DO NOT go on tangents asking for unrelated resources (like storage buckets) unless it directly correlates to the user's isolated request.
  
  To request additional data:
  - Use `list_available_resources` to see what other resource types are available
  - Think about what related resources might help provide more context
  - At the END of your response, output EXACTLY ONE of these tags:
    * <NEXT_RESOURCE>[resource_type]</NEXT_RESOURCE> - to collect a specific related resource type
    * <NEXT_RESOURCE>STOP</NEXT_RESOURCE> - when you have enough information
  """,
  tools=[list_available_resources]
)
