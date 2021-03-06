import zipfile, os

def apk2dex(src, dst, verbose=True):
    """
    Extract the classes.dex out of the apk and rename it to the apk filename.

    :param str src: source apk file
    :param str dst: destination folder to unzip
    :param bool verbose: Whether to print message.
    :return: None
    """
    target = "classes.dex"
    try:
        if not os.path.isdir(dst):
            os.makedirs(dst)
    except:
        raise ValueError("Incorrect output folder specified.")
    try:
        archive = zipfile.ZipFile(src)
        found = False
        for file in archive.namelist():
            if file == target:
                archive.extract(file, dst)
                found = True
                break
        if found:
            if verbose:
                print("Extracted file {}".format(src))
            os.rename(os.path.join(dst, target), os.path.join(dst, src.split("/")[-1][:-4] + ".dex"))
        else:
            raise zipfile.BadZipFile("No classes.dex found in file {}".format(src))
    except:
        raise zipfile.BadZipFile("Invalid or corrupted file {}".format(src))


def apk2dex_folder(src_dir, dst_dir, verbose=True, log=None):
    """
    Given a directory name, extract all the classes.dex inside the apks and rename it to the apk filename.

    :param str src_dir: The directory to extract its apk
    :param str dst_dir: The target directory to unzip
    :param bool verbose: Whether to print message and/or display progress bar.
    :param log: Whether to log unprocessed files in a log.
    :type log: str or None
    :return: None
    """
    bad_files = []
    apks = map(lambda x: os.path.join(src_dir, x), os.listdir(src_dir))
    has_tqdm = False
    if verbose:
        try:
            from tqdm import tqdm
            apks = tqdm(list(apks))
            has_tqdm = True
        except ImportError:
            pass
    for file in apks:
        if file[-4:] == ".apk":
            try:
                apk2dex(file, dst_dir, verbose and not has_tqdm)
            except zipfile.BadZipFile as e:
                if verbose:
                    if has_tqdm:
                        tqdm.write(str(e))
                    else:
                        print(str(e))
                bad_files.append(file)
    if log:
        with open(log, "w") as f:
            f.write("\n".join(bad_files))


if __name__ == "__main__":
    pass


