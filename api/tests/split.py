#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


class PDSplit(PaddleAPIBenchmarkBase):
    def build_program(self, config):
        data = self.variable(
            name='data', shape=config.input_shape, dtype=config.input_dtype)
        result = fluid.layers.split(
            input=data, num_or_sections=config.num_or_sections, dim=config.dim)

        self.feed_vars = [data]
        self.fetch_vars = [result]
        if config.backward:
            self.append_gradients(result, [data])


class TFSplit(TensorflowAPIBenchmarkBase):
    def build_graph(self, config):
        data = self.variable(
            name='data', shape=config.input_shape, dtype=config.input_dtype)
        result = tf.split(
            value=data,
            num_or_size_splits=config.num_or_sections,
            axis=config.dim)

        self.feed_list = [data]
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, [data])


if __name__ == '__main__':
    test_main(PDSplit(), TFSplit(), config=APIConfig("split"))
