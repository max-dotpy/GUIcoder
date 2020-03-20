from distutils.core import setup


setup(
  name = 'GUIcoder',
  packages = ['GUIcoder'],
  version = '0.15',
  license='MIT',
  description = 'Visual GUI code builder',
  author = 'Massimo Cosimo',
  author_email = 'pythonmax@hotmail.com',
  url = 'https://github.com/max-dotpy/GUI_maker',
  download_url = 'https://github.com/max-dotpy/GUI_maker/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['tkinter', 'GUI', 'Visual', 'builder', 'beginners-friendly'],
  install_requires=[
          'Pillow',
          'pyperclip',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
  entry_points={
        'console_scripts': [
            'GUIcoder= GUIcoder.app:main',
        ],
  },
)
