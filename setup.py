import setuptools

DEPENDENCIES = [
    'absl-py',
    'adafruit-circuitpython-bmp280',
    'adafruit-circuitpython-dotstar',
    'adafruit-circuitpython-motor',
    'apscheduler',
    'dropbox',
    'fire>=0.4.0',
    'google-cloud-speech',
    'keyboard',
    'mouse',
    'numpy',
    'parsedatetime',
    'redis',
    # selenium 4.0 breaks with arm geckodriver.
    'selenium==3.141.0',
    'sounddevice',
    'soundfile',
    'supervisor',
]

packages = [
    'gonotego',
    'gonotego.audio',
    'gonotego.command_center',
    'gonotego.common',
    'gonotego.leds',
    'gonotego.mouse',
    'gonotego.settings',
    'gonotego.text',
    'gonotego.transcription',
    'gonotego.uploader',
    'gonotego.uploader.blob',
    'gonotego.uploader.browser',
    'gonotego.uploader.ideaflow',
    'gonotego.uploader.mem',
    'gonotego.uploader.notion',
    'gonotego.uploader.remnote',
    'gonotego.uploader.roam',
]
setuptools.setup(
    name='GoNoteGo',
    version='1.0.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=packages,
    package_dir={d: d.replace('.', '/') for d in packages},
    python_requires='>=3.7',
    install_requires=DEPENDENCIES,
)
