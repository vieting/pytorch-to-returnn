"""
Utility to import a module with automatic Torch import wrapping, which replaces all::

  import torch

To::

  from pytorch_to_returnn import torch

In your user code, you would replace::

  import custom_torch_code

By::

  custom_torch_code = pytorch_to_returnn.wrapped_import.wrapped_import("custom_torch_code")

Both the wrapped and original module can be imported at the same time.
The wrapped module will internally get the full mod name ``pytorch_to_returnn._wrapped_mods.custom_torch_code``.
See :class:`_AstImportTransformer`.

"""

from typing import Union, Any
from .import_wrapper.base_wrappers.module import WrappedModule
from .import_wrapper.context import make_torch_default_ctx, make_torch_demo_ctx
from .import_wrapper.import_ import import_module


_ModPrefix = "%s._traced_torch." % __package__
_wrap_torch_ctx = make_torch_default_ctx(wrapped_mod_prefix=_ModPrefix)

_DemoModPrefix = "%s._torch_stub." % __package__
_wrap_torch_demo_ctx = make_torch_demo_ctx(wrapped_mod_prefix=_DemoModPrefix)


def wrapped_import(mod_name: str) -> Union[WrappedModule, Any]:  # rtype Any to make type checkers happy
  """
  :param str mod_name: full mod name, e.g. "custom_torch_code"
  :return: wrapped module
  """
  return import_module(mod_name, ctx=_wrap_torch_ctx)


def wrapped_import_demo(mod_name: str) -> Union[WrappedModule, Any]:  # rtype Any to make type checkers happy
  """
  :param str mod_name: full mod name, e.g. "custom_torch_code"
  :return: wrapped module
  """
  return import_module(mod_name, ctx=_wrap_torch_demo_ctx)
