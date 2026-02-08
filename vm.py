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

    def make_frame(self, code_obj, global_names, local_names):
        return "None"

    def run_frame(self, frame): ...
