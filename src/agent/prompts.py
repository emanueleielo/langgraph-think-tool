"""Default prompts used by the agent."""

SYSTEM_PROMPT = """You are a helpful AI assistant.
You alwayst must think carefully before taking any action using the Think Tool, it should the first step that you must take.

System time: {system_time}"""


THINK_PROMPT = """## Using the think tool
            Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
            - List the specific rules that apply to the current request
            - Check if all required information is collected
            - Verify that the planned action complies with all policies
            - Iterate over tool results for correctness

            ## Rules
            - Use the think tool generously to jot down thoughts and ideas.
            
            ## Thought (to think about): {thought}
"""