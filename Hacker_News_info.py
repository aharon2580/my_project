import sys
import csv
import requests
from tqdm import tqdm

HN_GENERAL = 'https://hacker-news.firebaseio.com/v0'
HN_ITEM = '/item/{}.json?print=pretty'
HN_TOP_STORIES = '/topstories.json?print=pretty'


def get_top_stories():
    response = requests.get(HN_GENERAL + HN_TOP_STORIES)
    if response.status_code == 200:
        return (response.json())


def get_story_info(story_id):
    response = requests.get(HN_GENERAL + HN_ITEM.format(story_id))
    if response.status_code == 200:
        return (response.json())


def all_stories_info(stories_id):
    info = []
    for story in stories_id[:5]:
        story_info = get_story_info(story)
        info.append(story_info)
    return info


def save_info(stories_info, file):
    keys = stories_info[0].keys()
    with open(file, 'w') as file:
        dict_wrietr = csv.DictWriter(file, keys, extrasaction='ignore')
        dict_wrietr.writeheader()
        dict_wrietr.writerows(stories_info)


def main():
    if len(sys.argv) < 2:
        raise ValueError('no file setis')
    file = sys.argv[1]
    stories_id = get_top_stories()
    stories_info = all_stories_info(stories_id)
    save_info(stories_info, file)
main()
