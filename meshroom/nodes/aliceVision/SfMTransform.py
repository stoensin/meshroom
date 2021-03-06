import sys
import os
from meshroom.core import desc


class SfMTransform(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_utils_sfmTransform {allParams}'
    size = desc.DynamicNodeSize('input')

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''SfMData file .''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='method',
            label='Transformation Method',
            description='''Transformation method (transformation, auto_from_cameras, auto_from_landmarks).''',
            value='auto_from_landmarks',
            values=['transformation', 'auto_from_cameras', 'auto_from_landmarks'],
            exclusive=True,
            uid=[0],
        ),
        desc.StringParam(
            name='transformation',
            label='Transformation',
            description='''Align [X,Y,Z] to +Y-axis, rotate around Y by R deg, scale by S; syntax: X,Y,Z;R;S. (required only for 'transformation' method)''',
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name='landmarksDescriberTypes',
            label='Landmarks Describer Types',
            description='''Image describer types used to compute the mean of the point cloud. (only for 'landmarks' method)''',
            value=['SIFT', 'SIFT_FLOAT', 'AKAZE', 'AKAZE_LIOP', 'AKAZE_MLDB', 'CCTAG3', 'CCTAG4', 'SIFT_OCV', 'AKAZE_OCV'],
            values=['SIFT', 'SIFT_FLOAT', 'AKAZE', 'AKAZE_LIOP', 'AKAZE_MLDB', 'CCTAG3', 'CCTAG4', 'SIFT_OCV', 'AKAZE_OCV'],
            exclusive=False,
            uid=[0],
            joinChar=',',
        ),
        desc.FloatParam(
            name='scale',
            label='Additional Scale',
            description='Additional scale to apply.',
            value=10.0,
            range=(1, 100.0, 1),
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='''Aligned SfMData file .''',
            value='{cache}/{nodeType}/{uid0}/transformedSfM.abc',
            uid=[],
        ),
    ]
