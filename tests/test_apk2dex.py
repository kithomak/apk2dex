import os, zipfile
import pytest

from apk2dex import apk2dex, apk2dex_folder


def test_apk2dex_sanity():
    src_dir = "tests/data/single_apk/"
    src_file = "single_test1.apk"
    dst_dir = "tests/temp/single_apk/"
    dst_file = "single_test1.dex"
    apk2dex(os.path.join(src_dir, src_file), dst_dir, verbose=False)
    assert len(os.listdir(dst_dir)) == 1, "apk2dex_sanity: apk2dex should only extract 1 file."
    assert os.path.isfile(os.path.join(dst_dir, dst_file)), "apk2dex_sanity: " \
                                                            "apk2dex should extract a single file correctly."
    assert os.stat(os.path.join(dst_dir, dst_file)).st_size == 5070244, "apk2dex_sanity: " \
                                                                        "apk2dex should extract a single file to correct size."

def test_apk2dex_incorrect_apk():
    with pytest.raises(zipfile.BadZipFile) as excinfo:
        src = "tests/data/bad_apks/bad_apk.apk"
        apk2dex(src, "tests/temp/bad_apk", verbose=False)
        assert str(excinfo.value) == "Invalid or corrupted file {}".format(src)

def test_apk2dex_no_dex_apk():
    with pytest.raises(zipfile.BadZipFile) as excinfo:
        src = "tests/data/bad_apks/no_dex.apk"
        apk2dex(src, "tests/temp/bad_apk", verbose=False)
        assert str(excinfo.value) == "No classes.dex found in file {}".format(src)

def test_apk2dex_incorrect_output_dir():
    with pytest.raises(ValueError) as excinfo:
        src = "tests/data/bad_apks/bad_apk.apk"
        apk2dex(src, src, verbose=False)
        assert str(excinfo.value) == "Incorrect output folder specified."

def test_apk2dex_folder_sanity():
    src_dir = "tests/data/multi_apk/"
    dst_dir = "tests/temp/multi_apk/"
    folder_size = 5
    apk2dex_folder(src_dir, dst_dir, verbose=True)  # for codecov purpose
    assert len(os.listdir(dst_dir)) == folder_size, "apk2dex_folder_sanity: apk2dex_folder should extract all files in a folder."
    for i in range(1, folder_size + 1):
        assert os.path.isfile(os.path.join(dst_dir, "multi_test{}.dex".format(i))), "apk2dex_folder_sanity: " \
                                                                                    "apk2dex_folder should extract files correctly."

def test_apk2dex_folder_log():
    src_dir = "tests/data/multi_apk/"
    dst_dir = "tests/temp/multi_apk/"
    log_file = "temp/log.txt"
    bad_apk = "bad_apk.apk"
    apk2dex_folder(src_dir, dst_dir, verbose=False, log=log_file)
    assert os.path.isfile(log_file), "apk2dex_folder_log: apk2dex_folder should create log file correctly."
    with open(log_file, "r") as f:
        content = f.read()
    assert content == os.path.join(src_dir, bad_apk), "apk2dex_folder_log: apk2dex_folder should log problematic files correctly."


