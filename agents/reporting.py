from google.adk.agents import LlmAgent

reporting_agent = LlmAgent(
  name='ReportingAgent',
  model='gemini-2.5-pro',
  description=(
      'Formats the toxic combinations into a formal full workflow security review.'
  ),
  instruction="""You are an executive security reporter. 
  Your job is to take the toxic combinations and findings synthesized by the SecurityAgent and format them into a highly readable, professional, and formal "Full Workflow Security Review" report. 
  
  Please organize the report clearly using Markdown headers. Consider including an Executive Summary, Detailed Findings (with Resources affected), and Recommended Remediations.
  Be precise, clear, and action-oriented. Do not ask follow-up questions to the user at the end of the report.
  """,
)
