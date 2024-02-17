# PyTezos Unknown Seed Issue

This repo demonstrates a `RpcError` in PyTezos when using `SandboxedNodeTestCase` for block baking. The error, appearing as `pytezos.rpc.node.RpcError: ({'id': 'proto.018-Proxford.seed.unknown_seed', 'kind': 'permanent', 'latest': 1, 'oldest': 0, 'requested': 2},)`, occurs around the 15th bake in tests, post-transition from Nairobinet to Oxfordnet.

## Running code:
```
poetry install
poetry run pytest test.py
```

