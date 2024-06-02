from setuptools import setup

package_name = 'tawnamy_control_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Andy Ponce',
    maintainer_email='andy.ponce@outlook.com',
    description='Package containing control demo scripts for tawnamy bot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_demo = tawnamy_control_demo.control_demo:main'
        ],
    },
)
