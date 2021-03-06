from meshroom.core import desc


class Ls(desc.CommandLineNode):
    commandLine = 'ls {inputValue} > {outputValue}'
    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''''',
            value='',
            uid=[0],
        )
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='''''',
            value='{cache}/{nodeType}/{uid0}/ls.txt',
            uid=[],
        )
    ]
