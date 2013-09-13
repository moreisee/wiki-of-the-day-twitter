#!/usr/bin/env python

import twitter
import wikipedia

def main():

    title, url, summary = get_random_wiki()

    post_len = title + "\n" + summary
    post = title + "\n" + summary + '\n' + url

    if len(post_len) > 110:
        title, summary = reduce_length(title, summary)
        post = title + "\n" + summary + '\n' +  url
    twitter_post(post)
    

def get_random_wiki():

    random_wiki = wikipedia.random()
    random_wiki_page = wikipedia.page(random_wiki)
    summary = wikipedia.summary(random_wiki, sentences=1)

    return random_wiki_page.title, random_wiki_page.url, summary

def twitter_post(post_data):
    api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

    status = api.PostUpdate(post_data)
    print(status.text)

def reduce_length(title, summary):
    if len(title) > 110:
        title = title[0:110] + '...'
        summary = ''
        return title, summary
    else:
        max_sum = 110 - len(title)
        summary = summary[0:max_sum] + '...'
        print(max_sum)
        print(summary)
        return title, summary


if __name__ == "__main__":
    main()

