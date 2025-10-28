def validate_response(response):
    if "Neil Armstrong" in response:
        return response
    return "Output did not meet guardrail criteria."
