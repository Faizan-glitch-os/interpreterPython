from frame import Frame


class VirtualMachineError(Exception):
    pass


class VirtualMachine:
    def __init__(self) -> None:
        self.frame_call_stack = []
        self.current_frame = None
        self.returned_value = None
        self.exception = None

    def run_code(self, code_obj, global_names=None, local_names=None):
        frame = self.make_frame(
            code_obj, global_names=global_names, local_names=local_names
        )

        self.run_frame(frame)

    def make_frame(self, code_obj, global_names, local_names, call_args={}):
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frame_call_stack:
            global_names = self.current_frame.global_names
            local_names = {}
        else:
            global_names = local_names = {
                "__builtins__": "__builtins__",
                "__name__": "__main__",
                "__doc__": None,
                "__package__": None,
            }

        local_names.update(call_args)

        frame = Frame(code_obj, local_names, global_names, self.current_frame)
        return frame

    def run_frame(self, frame): ...

    def push_frame(self, frame):
        self.frame_call_stack.append(frame)
        self.current_frame = frame

    def pop_frame(self):
        self.frame_call_stack.pop()
        if self.frame_call_stack:
            self.current_frame = self.frame_call_stack[-1]
        else:
            self.current_frame = None
