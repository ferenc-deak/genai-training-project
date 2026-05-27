class A2ARouter:
    """
    This is your real A2A boundary.
    It decides which agent receives the message.
    """

    def route(self, message, executor, external_executor):
        if message.context.get("use_external"):
            return external_executor.run(message.state)
        return executor.run(message.state)