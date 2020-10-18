import os
from pytube import YouTube

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=m53-rgMoPkU"
    try:
        title, is_ok = download_data(url)
    except Exception as e:
        print(str(e))
        print(url)
        print()

    crawl_result = {'url': url}
    yt = YouTube(url)
    streams = yt.streams
    crawl_result['title'] = yt.title

    folder_name = cln_txt(yt.title)
    target_folder = os.path.join('data', folder_name)
    os.mkdir(target_folder)

    targets = list()
    for item in streams:
        if item.resolution in res and item.mime_type == v_type:
            targets.append(item)
    res_cache = {'1080p':False, '720p':False}

