class Frame:
    def __init__(self, code_obj, local_names, global_names, previous_frame) -> None:
        self.code_obj = code_obj
        self.local_names = local_names
        self.global_names = global_names
        self.previous_frame = previous_frame

        self.data_stack = []
        self.block_stack = []
        self.last_instruction = 0

        if previous_frame:
            self.builtin_names = previous_frame.builtin_names
        else:
            self.builtin_names = local_names["__builtins__"]
            if hasattr(self.builtin_names, "__dict__"):
                self.builtin_names = self.builtin_names.__dict__
