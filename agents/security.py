from google.adk.agents import LlmAgent

security_agent = LlmAgent(
  name='SecurityAgent',
  model='gemini-2.5-pro',
  description=(
      'Reviews the security findings and cloud resource configurations and identifies toxic combinations.'
  ),
  instruction="""
  You are a cloud security expert. You should review the security findings and cloud configurations provided to you and try to group them to identify toxic combinations that are not immediately obvious from individual findings. 
  You should draw deep insights and focus on reporting big picture macro issues rather than individual findings or misconfigurations, but you should always reference the resources and findings in each of your issue items.
  """,
)
