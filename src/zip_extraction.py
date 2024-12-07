import zipfile
import os
import pathlib

def extract_zip_with_japanese(zip_file_path: str, extract_path: str) -> None:
    """
    zipファイル解凍関数

    Args:
        zip_file_path (str): zipファイルのパス
        extract_path (str): 解凍先のディレクトリパス
    
    Returns:
        None
    
    Raises:
    zipfile.BadZipFile: zipファイルが壊れている場合
    FileNotFoundError: zipファイルが存在しない場合
    """

    #出力フォルダがない場合は作成する
    pathlib.Path(extract_path).mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            for info in zip_ref.infolist():
                try:
                    if hasattr(info, 'flag_bits') and info.flag_bits & 0x800:
                        filename = info.filename
                    else:
                        filename = info.filename.encode('cp437').decode('cp932')
                except UnicodeDecodeError:
                    filename = info.filename

                # ファイル名として使えない文字は置換
                filename = filename.replace(':', '_').replace('*', '_').replace('?', '_')\
                                 .replace('"', '_').replace('<', '_').replace('>', '_')\
                                 .replace('|', '_')
                
                target_path = os.path.join(extract_path, filename)

                # 出力先フォルダの作成
                if filename.endswith('/'):
                    pathlib.Path(target_path).mkdir(parents=True, exist_ok=True)
                    continue

                parent_dir = os.path.dirname(target_path)
                if parent_dir :
                    pathlib.Path(parent_dir).mkdir(parents=True, exist_ok=True)

                with zip_ref.open(info) as source, open(target_path, "wb") as target:
                    target.write(source.read())

    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"{zip_file_path} は不正なzipファイルです。")
    except FileNotFoundError:
        raise FileNotFoundError(f"{zip_file_path} は存在しません。")


if __name__ == "__main__":
    # テスト用のzipファイルを作成
    zip_file_path = "test.zip"
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        zip_file.writestr("日本語ファイル名.txt", "こんにちは、世界！")

    extract_zip_with_japanese(zip_file_path, "output")