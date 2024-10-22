
import hyperSel
import scrapetube 

def fix_title(temp_title):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789 .-_'
    return ''.join(c for c in temp_title if c.isalnum() or c.isspace() or c in allowed_chars)

def fix_desc(temp_description):
    desc = ''.join((e for e in temp_description
                    if e.isalnum() or e.isspace() and e not in ["'", '"', ',', '(', ')', '``', '`', '\\', "'", '"', ',', '_', '*', '~', '[', ']', '{', '}', ';', '+', '=', '?', '<', '>', '&', '|', '$', '#', '%', '^']))
    return desc

def get_all_youtube_channel_content_by_channel_id(channel_id):
    videos = scrapetube.get_channel(f"{channel_id}")
    posts = []
    for video in videos:
        try:
            video_id = video['videoId']
            template = "https://www.youtube.com/watch?v=@VIDEO_ID"

            title = fix_title(video['title']['runs'][0]['text'])
            desc = fix_desc(video['descriptionSnippet']['runs'][0]['text'])
            url = template.replace("@VIDEO_ID", video_id)
            posts.append([title, desc, url])
        except:
            continue
    return posts

if __name__ == '__main__':
    print("hello world")
