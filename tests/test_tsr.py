#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from time import sleep
import pytest
from pynq import MMIO
from pynq import Overlay
#from pynq import general_const
import tsr
from pynq import Xlnk
from PIL import Image

# Testing LFC with MNIST dataset - HW
def test_mnist():
	BNN_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

	test_image_mnist   = os.path.join(BNN_ROOT_DIR, 'Test_image', '3.image-idx3-ubyte')

	classifier = tsr.TSR(network=bnn.NETWORK_LFC)
	classifier.load_parameters("mnist")
	out = classifier.inference(test_image_mnist)
	assert out==3, \
		'MNIST HW test failed'
	# Testing LFC with MNIST dataset - SW
	
	classifier_sw = tsr.TSR(network=tsr.NETWORK_LFC,runtime=tsr.RUNTIME_SW)
	classifier_sw.load_parameters("mnist")
	out_sw = classifier_sw.inference(test_image_mnist)

	assert out_sw==3, \
		'MNIST SW test failed'

	xlnk = Xlnk()
	xlnk.xlnk_reset()

def test_cifar10():
	BNN_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

	test_image_cifar10 = os.path.join(BNN_ROOT_DIR, 'Test_image', 'deer.jpg')

	im = Image.open(test_image_cifar10)
	classifier = tsr.CnvClassifier('cifar10')
	out=classifier.classify_image(im)

	assert out==4, \
		'Cifar10 HW test failed'

	classifier_sw = tsr.CnvClassifier("cifar10", tsr.RUNTIME_SW)
	out_sw = classifier_sw.classify_image(im)

	assert out==4, \
		'Cifar10 SW test failed'
	
	xlnk = Xlnk();
	xlnk.xlnk_reset()

def test_svhn():

	BNN_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

	test_image_svhn = os.path.join(BNN_ROOT_DIR, 'Test_image', '6.png')
	
	im = Image.open(test_image_svhn)
	classifier = tsr.CnvClassifier('streetview')
	out=classifier.classify_image(im)

	assert out==5, \
		'SVHN HW test failed'
	
	classifier_sw = tsr.CnvClassifier("streetview", tsr.RUNTIME_SW)
	out_sw = classifier_sw.classify_image(im)

	assert out== 5, \
		'SVHN SW test failed'
	
	xlnk = Xlnk();
	xlnk.xlnk_reset()


def test_road_sign():

	BNN_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

	test_image_road = os.path.join(BNN_ROOT_DIR, 'Test_image', 'stop.jpg')

	im = Image.open(test_image_road)
	classifier = tsr.CnvClassifier('road-signs')
	out=classifier.classify_image(im)

	assert out==14, \
		'Road sign HW test failed'
	
	classifier_sw = tsr.CnvClassifier("road-signs", tsr.RUNTIME_SW)
	out_sw = classifier_sw.classify_image(im)

	assert out== 14, \
		'Road sign SW test failed'
	
	xlnk = Xlnk();
	xlnk.xlnk_reset()
