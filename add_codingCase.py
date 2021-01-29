# 增加coding测试用例
import requests
class api:

    def __init__(self, HOSTNAME, Cookie):
        self.HOSTNAME = HOSTNAME
        self.Cookie = Cookie

    def userApi(self, path, ContentType, params):
        url = "https://" + self.HOSTNAME + path
        print(url)
        headers = {  # 设置http头部信息
            'Host': self.HOSTNAME,
            'Cookie': self.Cookie,
            'Content-Type': ContentType,
            'Sec-Fetch-Site':'same-ori',
            'X-XSRF-TOKEN':'c16b2954-7b13-4fdf-a7c3-bd7c208dbdc4',
            'Content-Length':'81',
            'Connection':'keep-alive'

        }
        # json格式
        # print(url)
        results = requests.post(url, headers=headers, json=params).text
        print(results)
        return results
        # self.assertResult(results)

class addApi():
    def __init__(self,title):
        HOSTNAME = 'theling.coding.net'

        # 合同列表
        Cookie = 'united=24c4bcb1-dfb3-4c06-9754-2420841c91d5; _ga=GA1.2.862775069.1591579907; enterprise_domain=theling; eid=aabf0e54-ec67-403b-9e8c-50a44c12593d; code=agent%3Dtrue%2Cartifacts-overview%3Dtrue%2Cartifacts-properties%3Dtrue%2Cartifacts-scan%3Dtrue%2Cartifacts-strategy%3Dtrue%2Casync-blocked%3Dtrue%2Cci-micro-frontend%3Dtrue%2Cci-new-visualization-pipeline%3Dtrue%2Cci-team-step%3Dfalse%2Cci-team-templates%3Dtrue%2Ccoding-flow%3Dfalse%2Ccoding-ocd-java%3Dfalse%2Ccoding-ocd-pages%3Dtrue%2Ccomposer-proxy%3Dtrue%2Cjob-refresh%3Dtrue%2Cmobile-layout-test%3Dfalse%2Cnew-public-artifacts%3Dfalse%2Conan%3Dtrue%2Cservice-exception-tips%3Dfalse%2Cstatic-website%3Dtrue%2Cteam-agent%3Dtrue%2Ctencent-cloud-object-storage%3Dtrue%2C5b585356; exp=89cd78c2; c=ci-team-templates%3Dtrue%2Cagent%3Dtrue%2Cartifacts-overview%3Dtrue%2Cartifacts-properties%3Dtrue%2Cartifacts-scan%3Dtrue%2Cartifacts-strategy%3Dtrue%2Cci-micro-frontend%3Dtrue%2Cci-new-visualization-pipeline%3Dtrue%2Ccomposer-proxy%3Dtrue%2Cjob-refresh%3Dtrue%2Conan%3Dtrue%2Cstatic-website%3Dtrue%2Cteam-agent%3Dtrue%2C080f5651; _gid=GA1.2.532987119.1610328778; XSRF-TOKEN=c16b2954-7b13-4fdf-a7c3-bd7c208dbdc4; coding_demo_visited=1; io=Bor7MOrM_S4hVdJMAEIj; coding_testing_production_session=eyJpdiI6ImlOdFBCZHpDYWpEZjhNdHpOajJ0Z2c9PSIsInZhbHVlIjoiQm1XR3dkbzJIM1VzNUVWNVVMQTVWV015YWNHaFwvSHNcL0ozUGw5ZDJWQkFxUCt1T3JxVkkwRXU4eTNWZk5CQkJ6IiwibWFjIjoiNDYzNmI0Y2M2YjcwMTY3MjJmMzBlYmE3OTM1NmVhOWFjNzVlMzJlZTI3ZGYyZjdhZmZiMmU4ZTg5OGMwMWEwYSJ9'
        path = '/testing/api/v1/projects/prepayment-serve/cases'
        ContentType = "application/json"
        api1 = api(HOSTNAME, Cookie)
        params = {"title": title, "section_id": 601524, "priority": 2, "template_type": "TEXT"}
        results = api1.userApi(path, ContentType, params)

if __name__ == "__main__":
    HOSTNAME = 'theling.coding.net'

    # 合同列表
    Cookie='united=24c4bcb1-dfb3-4c06-9754-2420841c91d5; _ga=GA1.2.862775069.1591579907; enterprise_domain=theling; eid=aabf0e54-ec67-403b-9e8c-50a44c12593d; code=agent%3Dtrue%2Cartifacts-overview%3Dtrue%2Cartifacts-properties%3Dtrue%2Cartifacts-scan%3Dtrue%2Cartifacts-strategy%3Dtrue%2Casync-blocked%3Dtrue%2Cci-micro-frontend%3Dtrue%2Cci-new-visualization-pipeline%3Dtrue%2Cci-team-step%3Dfalse%2Cci-team-templates%3Dtrue%2Ccoding-flow%3Dfalse%2Ccoding-ocd-java%3Dfalse%2Ccoding-ocd-pages%3Dtrue%2Ccomposer-proxy%3Dtrue%2Cjob-refresh%3Dtrue%2Cmobile-layout-test%3Dfalse%2Cnew-public-artifacts%3Dfalse%2Conan%3Dtrue%2Cservice-exception-tips%3Dfalse%2Cstatic-website%3Dtrue%2Cteam-agent%3Dtrue%2Ctencent-cloud-object-storage%3Dtrue%2C5b585356; exp=89cd78c2; c=ci-team-templates%3Dtrue%2Cagent%3Dtrue%2Cartifacts-overview%3Dtrue%2Cartifacts-properties%3Dtrue%2Cartifacts-scan%3Dtrue%2Cartifacts-strategy%3Dtrue%2Cci-micro-frontend%3Dtrue%2Cci-new-visualization-pipeline%3Dtrue%2Ccomposer-proxy%3Dtrue%2Cjob-refresh%3Dtrue%2Conan%3Dtrue%2Cstatic-website%3Dtrue%2Cteam-agent%3Dtrue%2C080f5651; _gid=GA1.2.532987119.1610328778; XSRF-TOKEN=c16b2954-7b13-4fdf-a7c3-bd7c208dbdc4; coding_demo_visited=1; io=Bor7MOrM_S4hVdJMAEIj; coding_testing_production_session=eyJpdiI6ImlOdFBCZHpDYWpEZjhNdHpOajJ0Z2c9PSIsInZhbHVlIjoiQm1XR3dkbzJIM1VzNUVWNVVMQTVWV015YWNHaFwvSHNcL0ozUGw5ZDJWQkFxUCt1T3JxVkkwRXU4eTNWZk5CQkJ6IiwibWFjIjoiNDYzNmI0Y2M2YjcwMTY3MjJmMzBlYmE3OTM1NmVhOWFjNzVlMzJlZTI3ZGYyZjdhZmZiMmU4ZTg5OGMwMWEwYSJ9'
    path = '/testing/api/v1/projects/prepayment-serve/cases'
    ContentType = "application/json"
    api1 = api(HOSTNAME, Cookie)
    params = {"title":"测试用例5","section_id":589129,"priority":2,"template_type":"TEXT"}
    results = api1.userApi(path, ContentType, params)
