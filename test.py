from pytezos.sandbox.node import SandboxedNodeTestCase

class BaseTestCase(SandboxedNodeTestCase):
    def test_should_allow_to_bake_many_blocks(self) -> None:
        for block in range(100):
            self.bake_block()
            print(f'baked block #{block}')

