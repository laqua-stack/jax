# Copyright 2022 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note that type annotations for this file are defined in basearray.pyi

import abc

class Array(abc.ABC):
  """Array base class for JAX

  ``jax.Array`` is the public interface for instance checks and type annotation of JAX
  arrays and tracers. Its main applications are in instance checks and type annotations;
  for example::

    x = jnp.arange(5)
    isinstance(x, jax.Array)  # returns True both inside and outside traced functions.

    def f(x: Array) -> Array:  # type annotations are valid for traced and non-traced types.
      return x

  Because `jax.Array` is effectively an abstact base class, the main documentation for
  its methods is not here, but rather at :mod:`jax.numpy`.
  """
  # Note: no abstract methods are defined in this base class; the associated pyi
  # file contains the type signature for static type checking.

  __slots__ = ['__weakref__']

  # at property must be defined because we overwrite its docstring in lax_numpy.py
  @property
  def at(self):
    raise NotImplementedError("property must be defined in subclasses")


Array.__module__ = "jax"
