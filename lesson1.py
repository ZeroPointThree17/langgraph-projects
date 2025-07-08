from typing_extensions import TypedDict  
from langgraph.graph import StateGraph, START, END


# Define the state structure  
class HelloWorldState(TypedDict):  
    greeting: str # This key will store the greeting message

# Define the node function
def hello_world_node(state: HelloWorldState):
    state["greeting"] = "Hello World, " + state["greeting"]
    return state