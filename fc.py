#with function call
chat_response = chat_completion_request(
    conversation.conversation_history,
    functions = functions
)

chat_response.json()