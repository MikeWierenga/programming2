import webcrawler

# test = webcrawler.Crawler()
# for x in range(5):
#     print(str(next(test)))

crawler = webcrawler.Crawler()

for result in crawler:

    print(result)