import tempfile
import filecmp
import os
import unittest

from stltovoxel import doExport


class TestStlToVoxel(unittest.TestCase):
    def test_sample(self):
        with tempfile.TemporaryDirectory() as tmpDir:
            # https://commons.wikimedia.org/wiki/File:Stanford_Bunny.stl
            doExport('data/Stanford_Bunny.stl', os.path.join(tmpDir, 'stanford_bunny.png'), 100)
            # https://ozeki.hu/p_1116-sample-stl-files-you-can-use-for-testing.html
            doExport('data/Cube_3d_printing_sample.stl', os.path.join(tmpDir, 'Cube_3d_printing_sample.png'), 100)
            doExport('data/Menger_sponge_sample.stl', os.path.join(tmpDir, 'Menger_sponge_sample.png'), 100)
            doExport('data/Eiffel_tower_sample.STL', os.path.join(tmpDir, 'Eiffel_tower_sample.png'), 100)
            # https://reprap.org/forum/read.php?88,6830
            doExport('data/HalfDonut.stl', os.path.join(tmpDir, 'HalfDonut.png'), 100)
            doExport('data/Star.stl', os.path.join(tmpDir, 'Star.png'), 100)
            doExport('data/Moon.stl', os.path.join(tmpDir, 'Moon.png'), 100)

    def test_issue_files(self):
        with tempfile.TemporaryDirectory() as tmpDir:
            # Provided by @silverscorpio in issue #16
            doExport('data/test1.stl', os.path.join(tmpDir, 'test1.png'), 100)
            # Provided by @silverscorpio in PR #18
            doExport('data/test2.stl', os.path.join(tmpDir, 'test2.png'), 100)

    def test_resolution(self):
        with tempfile.TemporaryDirectory() as tmpDir:
            for i in range(1, 100):
                print('resolution:', i)
                doExport('data/Pyramid.stl', os.path.join(tmpDir, 'Pyramid.png'), i)

    def test_doExport(self):
        with tempfile.TemporaryDirectory() as tmpDir:
            outputFile = os.path.join(tmpDir, 'stanford_bunny.png')
            doExport('data/Stanford_Bunny.stl', outputFile, 100)
            expectedFiles = sorted(os.listdir('data/stanford_bunny_golden_slices'))
            actualFiles = sorted(os.listdir(tmpDir))

    def test_resolution():
        for i in range(1, 100):
            print('resolution:', i)
            with tempfile.TemporaryDirectory() as tmpDir:
                doExport('data/Pyramid.stl', os.path.join(tmpDir, 'Pyramid.png'), i)
                doExport('data/Menger_sponge_sample.stl', os.path.join(tmpDir, 'Menger_sponge_sample.png'), i)
                doExport('data/Eiffel_tower_sample.STL', os.path.join(tmpDir, 'Eiffel_tower_sample.png'), i)
