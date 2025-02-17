# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2021 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------


class EvalInfo(object):
    """
    Evaluate node properties and parameters
    """
    def __init__(self, node):
        if node is None:
            raise TypeError
        self.node = node

    def EvaluateParameter(self, name):
        """ Evaluates the value of a parameter. """
        param = self.node._parameters[name]
        if param.binding:
            # Evaluate the next node
            info = EvalInfo(param.binding)
            return param.binding.EvaluateNode(info)
        return param.value

    def EvaluateProperty(self, name):
        """ Evaluates the value of a property. """
        prop = self.node._properties[name]
        return prop.value
