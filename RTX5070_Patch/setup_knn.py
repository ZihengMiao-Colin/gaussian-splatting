# 文件位置: E:\3dGS\gaussian-splatting\submodules\simple-knn\setup.py
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os

setup(
    name='simple_knn',
    ext_modules=[
        CUDAExtension(
            name='simple_knn._C',
            sources=[
                'spatial.cu', 
                'simple_knn.cu',
                'ext.cpp'
            ],
            extra_compile_args={
                'cxx': ['/permissive-', '-O3'], 
                'nvcc': [
                    '-O3', 
                    '-Xcompiler', '/permissive-',
                    # ===================================================
                    # 关键修改：注意这里是 code=compute_89
                    # 这会让驱动在运行时动态生成适配 RTX 5070 的指令
                    # ===================================================
                    '-gencode=arch=compute_89,code=compute_89'
                ]
            }
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)