# 文件: submodules/diff-gaussian-rasterization/setup.py
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
glm_path = os.path.join(current_dir, "third_party", "glm")

setup(
    name="diff_gaussian_rasterization",
    packages=['diff_gaussian_rasterization'],
    ext_modules=[
        CUDAExtension(
            name="diff_gaussian_rasterization._C",
            sources=[
            "cuda_rasterizer/rasterizer_impl.cu",
            "cuda_rasterizer/forward.cu",
            "cuda_rasterizer/backward.cu",
            "rasterize_points.cu",
            "ext.cpp"],
            extra_compile_args={
                'cxx': ['/permissive-', '-O3'], 
                'nvcc': [
                    '-O3', 
                    '-Xcompiler', '/permissive-',
                    # ===============================================
                    # 关键修改：启用 PTX (JIT)，适配 RTX 5070
                    # ===============================================
                    '-gencode=arch=compute_89,code=compute_89'
                ]
            },
            include_dirs=[glm_path]
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)