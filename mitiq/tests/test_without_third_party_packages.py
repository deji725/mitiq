# Copyright (C) Unitary Fund
#
# This source code is licensed under the GPL license (v3) found in the
# LICENSE file in the root directory of this source tree.

"""Tests to make sure Mitiq works without optional packages like Qiskit,
pyQuil, etc.

Ideally these tests should touch all of Mitiq except for
mitiq.interface.mitiq_[package], where [package] is any supported package that
interfaces with Mitiq (see mitiq.SUPPORTED_PROGRAM_TYPES).
"""
from abc import ABCMeta


def test_import():
    """Simple test that Mitiq can be imported without any (or all) supported
    program types.
    """
    import mitiq

    if isinstance(mitiq.QPROGRAM, ABCMeta):
        pass  # If only Cirq is installed, QPROGRAM is not a typing.Union.
    else:
        assert (
            1  # cirq.Circuit is always supported.
            <= len(mitiq.QPROGRAM.__args__)  # All installed types.
            <= len(mitiq.SUPPORTED_PROGRAM_TYPES.keys())  # All types.
        )


# TODO: More tests wanted!
