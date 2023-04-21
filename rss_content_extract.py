import feedparser


rss_url = "https://www.msit.go.kr/user/rss/rss.do?bbsSeqNo=96" # 읽어올 RSS 피드 URL
feed = feedparser.parse(rss_url)

# 각 항목(entry)마다 정보 출력
for entry in feed.entries:
    print("제목: ", entry.title)
    print("링크: ", entry.link)
    print("발행일: ", entry.updated) #pudDate 대신 updated
    print()
