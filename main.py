import requests
import re
import openpyxl
import time

#爬抖音热榜
headers = {
    'Referer': 'https://www.douyin.com/discover?enter=guide',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Cookie': 'ttwid=1%7CBuhkbYw7_gcVbYvpjZ6DpemgJujaliaArP0V3thgxHo%7C1707911268%7C810aeb71aaaddc9c99b1ae12b82db86c989e6e5415f31cb778bf54ba172f1df3; dy_swidth=1536; dy_sheight=864; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; passport_csrf_token=6b6815730c09426eb9d9535e3644add1; passport_csrf_token_default=6b6815730c09426eb9d9535e3644add1; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; xgplayer_user_id=481351203845; bd_ticket_guard_client_web_domain=2; ttcid=1286122a90134de18a9e4842dd20002412; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=a3qKpgw_wY4VIjqCQaHfjOESIHAdtV5c86zW4X1cJpU; sso_auth_status=3751f307fe7884eaa185997f31a6b0b7; sso_auth_status_ss=3751f307fe7884eaa185997f31a6b0b7; publish_badge_show_info=%220%2C0%2C0%2C1708002486368%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; pwa2=%220%7C0%7C3%7C0%22; passport_assist_user=CkFQ1DguP3SQiueS2-i_G8yxRk3nzCT8lsdazX2IwMZMc7NNJVpHdJsuV4Kdurf4ND2DkoS4QUoSIltdf0lJ9pDYUhpKCjwF42mRQ8mV4wzP7WsRuPFCYIELIGdQ0IWaCG4LqV-VE6p5QEKRKoGOfHo-TClQsVK6OGrTa5wwB5FxnL4QnbrJDRiJr9ZUIAEiAQNrpuE5; sso_uid_tt=5d76a41394c86a31085db7de562ca21e; sso_uid_tt_ss=5d76a41394c86a31085db7de562ca21e; toutiao_sso_user=6f5c61e6c5bcd4ab8b145c0f8433b362; toutiao_sso_user_ss=6f5c61e6c5bcd4ab8b145c0f8433b362; sid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; ssid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; passport_auth_status=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; passport_auth_status_ss=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; uid_tt=6e9bbf84ea26c7a66c5fb11ddd33d448; uid_tt_ss=6e9bbf84ea26c7a66c5fb11ddd33d448; sid_tt=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid_ss=44629b269b0c550b5f0b5cbfb23fe3f7; _bd_ticket_crypt_cookie=bab77e18608c83d5ae0a841912e3272f; sid_guard=44629b269b0c550b5f0b5cbfb23fe3f7%7C1708005323%7C5183998%7CMon%2C+15-Apr-2024+13%3A55%3A21+GMT; sid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; ssid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; csrf_session_id=3864ddcfe25c1ff249ffcc8bb7977ffc; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183151603%2F0%22; strategyABtestKey=%221708183152.173%22; xg_device_score=6.794335695120184; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183155063%2F0%22; tt_scid=lV-y8l.RQP0thpFVkC-b1uhoxtkIKc5TEZkX.2L4V9KoimKeedXvEoTAiJfSeYiR9f39; download_guide=%223%2F20240217%2F1%22; __ac_nonce=065d0cec7001dd5b6f2ae; __ac_signature=_02B4Z6wo00f01y2EMOgAAIDAEC0qdX.WF3stpDRAAK68EQFQWSthN4tqN9EIw.qWoeg0R4hVz3AOXFvNNj-VGBx.555zY4cTY.2a3xlGgWF5NiByZMu3f7jlRuwGNPZ7pqMCU44n9Mjr1Uibd3; SEARCH_RESULT_LIST_TYPE=%22single%22; odin_tt=8b24a8020edb289f49677cfdfe1199d89a171065c41830d57df274d51750414d115e35672bf5f8e53361f3caf7a59ae6; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.5%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTThwbXExU2dUM1ZDWXpxZnhEbjViUmhGdnFXTWdpNzdZN1IwejE1S2hWajZqZlJrTmhTamN6QldWeHgwSGd0YTBHR3JvMzYzTzB0aUlkN2hDVW9JQ009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=yPoIvIY4_YaT5iY99h8XJ_raQ8PB1gKxKb38N8sTRk6J_SKq0XlLiIu8cWm0QdKn5qu-Ed7gZjgRx36lw7Y5FjrhKzG5rt5SxDwzbJHo48ZHPWXDOiJDL0LsTNA=; msToken=aYGxNWM9yPc4e1MaHVOuIWbn9Gvmi-g2nJM4dU4Bn1jG52eXbXeH9HpfOdbbLX58vXssoXx1An_0eGRpLWqmpuGwEVH2vf61vGfuvAAEhDGL0IWVmg=='
}
url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&board_type=0&board_sub_type=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=1.5&effective_type=4g&round_trip_time=50&webid=7335422965398914560&msToken=yPoIvIY4_YaT5iY99h8XJ_raQ8PB1gKxKb38N8sTRk6J_SKq0XlLiIu8cWm0QdKn5qu-Ed7gZjgRx36lw7Y5FjrhKzG5rt5SxDwzbJHo48ZHPWXDOiJDL0LsTNA=&X-Bogus=DFSzswVYA5bANG7HtofQivB9PimS'
data = requests.get(url, headers=headers).text
pat = re.compile(
    '"word_sub_board".*?"event_time":(.*?),"group_id":.*?,"hot_value":(.*?),"hotlist_param".*?"sentence_id":"(.*?)","sentence_tag".*?"word":"(.*?)","word_cover"')
text = pat.findall(data)

bas = 'http://www.douyin.com/hot/'
text2 = []
for i in text:
    j = list(i)
    j[2] = bas + j[2]
    text2.append(j)
count = 0
for i in range(len(text2)):
    if text2[i][1] == '0':
        count += 1
    else:
        break
new_text = text2[count:]
for i in range(len(new_text)):
    new_text[i].insert(0, str(i+1))

new_text.insert(0, ['排名', '时间', '热度', '链接', '标题'])
wb = openpyxl.Workbook()
ws = wb.active
for element in new_text:
    ws.append(element)
ws.column_dimensions['B'].width = 15
ws.column_dimensions['C'].width = 10
ws.column_dimensions['D'].width = 35
ws.column_dimensions['E'].width = 30
wb.save('抖音热榜top50实时数据.xlsx')



'''
#爬取抖音视频
headers = {
    'Referer': 'https://www.douyin.com/channel/300205',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Cookie': 'ttwid=1%7CBuhkbYw7_gcVbYvpjZ6DpemgJujaliaArP0V3thgxHo%7C1707911268%7C810aeb71aaaddc9c99b1ae12b82db86c989e6e5415f31cb778bf54ba172f1df3; dy_swidth=1536; dy_sheight=864; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; passport_csrf_token=6b6815730c09426eb9d9535e3644add1; passport_csrf_token_default=6b6815730c09426eb9d9535e3644add1; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; xgplayer_user_id=481351203845; bd_ticket_guard_client_web_domain=2; ttcid=1286122a90134de18a9e4842dd20002412; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=a3qKpgw_wY4VIjqCQaHfjOESIHAdtV5c86zW4X1cJpU; sso_auth_status=3751f307fe7884eaa185997f31a6b0b7; sso_auth_status_ss=3751f307fe7884eaa185997f31a6b0b7; publish_badge_show_info=%220%2C0%2C0%2C1708002486368%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; pwa2=%220%7C0%7C3%7C0%22; passport_assist_user=CkFQ1DguP3SQiueS2-i_G8yxRk3nzCT8lsdazX2IwMZMc7NNJVpHdJsuV4Kdurf4ND2DkoS4QUoSIltdf0lJ9pDYUhpKCjwF42mRQ8mV4wzP7WsRuPFCYIELIGdQ0IWaCG4LqV-VE6p5QEKRKoGOfHo-TClQsVK6OGrTa5wwB5FxnL4QnbrJDRiJr9ZUIAEiAQNrpuE5; sso_uid_tt=5d76a41394c86a31085db7de562ca21e; sso_uid_tt_ss=5d76a41394c86a31085db7de562ca21e; toutiao_sso_user=6f5c61e6c5bcd4ab8b145c0f8433b362; toutiao_sso_user_ss=6f5c61e6c5bcd4ab8b145c0f8433b362; sid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; ssid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; passport_auth_status=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; passport_auth_status_ss=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; uid_tt=6e9bbf84ea26c7a66c5fb11ddd33d448; uid_tt_ss=6e9bbf84ea26c7a66c5fb11ddd33d448; sid_tt=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid_ss=44629b269b0c550b5f0b5cbfb23fe3f7; _bd_ticket_crypt_cookie=bab77e18608c83d5ae0a841912e3272f; sid_guard=44629b269b0c550b5f0b5cbfb23fe3f7%7C1708005323%7C5183998%7CMon%2C+15-Apr-2024+13%3A55%3A21+GMT; sid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; ssid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; csrf_session_id=3864ddcfe25c1ff249ffcc8bb7977ffc; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183151603%2F0%22; strategyABtestKey=%221708183152.173%22; xg_device_score=6.794335695120184; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183155063%2F0%22; tt_scid=lV-y8l.RQP0thpFVkC-b1uhoxtkIKc5TEZkX.2L4V9KoimKeedXvEoTAiJfSeYiR9f39; download_guide=%223%2F20240217%2F1%22; __ac_nonce=065d0cec7001dd5b6f2ae; __ac_signature=_02B4Z6wo00f01y2EMOgAAIDAEC0qdX.WF3stpDRAAK68EQFQWSthN4tqN9EIw.qWoeg0R4hVz3AOXFvNNj-VGBx.555zY4cTY.2a3xlGgWF5NiByZMu3f7jlRuwGNPZ7pqMCU44n9Mjr1Uibd3; SEARCH_RESULT_LIST_TYPE=%22single%22; odin_tt=8b24a8020edb289f49677cfdfe1199d89a171065c41830d57df274d51750414d115e35672bf5f8e53361f3caf7a59ae6; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.5%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTThwbXExU2dUM1ZDWXpxZnhEbjViUmhGdnFXTWdpNzdZN1IwejE1S2hWajZqZlJrTmhTamN6QldWeHgwSGd0YTBHR3JvMzYzTzB0aUlkN2hDVW9JQ009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=yPoIvIY4_YaT5iY99h8XJ_raQ8PB1gKxKb38N8sTRk6J_SKq0XlLiIu8cWm0QdKn5qu-Ed7gZjgRx36lw7Y5FjrhKzG5rt5SxDwzbJHo48ZHPWXDOiJDL0LsTNA=; msToken=aYGxNWM9yPc4e1MaHVOuIWbn9Gvmi-g2nJM4dU4Bn1jG52eXbXeH9HpfOdbbLX58vXssoXx1An_0eGRpLWqmpuGwEVH2vf61vGfuvAAEhDGL0IWVmg=='
}


#1.游戏区
url = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&tag_id=300205&count=10&Seo-Flag=0&refresh_index=1&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7335422965398914560&msToken=87aXzHf-n3n5FN9pxngYV1bxja4ecoYpUuJvE1tQLVI3mmye7agUNIZJ2FzkkiRaHmr6o-6WQa1MqcbhIzoNJS6XmirRkjDU1uMiC3fA0m-05gd0FWCgqhkEStE=&X-Bogus=DFSzswVuCQiANxbWtoXV/vB9PiFU'
data = requests.get(url, headers=headers).text
pat = re.compile('"url_list":\["http://v3-web.douyinvod.com/(.*?)\\\\')
target = pat.search(data)
path = 'http://v3-web.douyinvod.com/' + target.group(1)
my_video = requests.get(path, headers=headers).content
with open('游戏区第一个视频.mp4', 'wb') as f:
    f.write(my_video)
time.sleep(3)

#2.美食区
url2 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&tag_id=300204&count=10&Seo-Flag=0&refresh_index=1&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7335422965398914560&msToken=Y6R3dHtbKBnvF1lIfeWLoQU6-xtWiGUfLiilAKVwP0pkhqqQgK0zYkKTQPnzOsuPg7yO7uAAhBeTMQsPrws-2-XCPq3tkDDSID7NY7cvrxlA_zIneMxF3-hysVk=&X-Bogus=DFSzswVYIysANG7Hto6/JiB9Piur'
data2 = requests.get(url2, headers=headers).text
pat2 = re.compile('"url_list":\["http://v3-web.douyinvod.com/(.*?)\\\\')
target2 = pat2.search(data2)
path2 = 'http://v3-web.douyinvod.com/' + target2.group(1)
my_video2 = requests.get(path2, headers=headers).content
with open('美食区第一个视频.mp4', 'wb') as f:
    f.write(my_video2)
time.sleep(3)

#3.知识区
url3 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=16&tag_id=300213&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7335422965398914560&msToken=UZ7kmrCGTBKcnJ9_0n8QH94tPLtrxBMGIPbZtHmUE-JqjJF9aIeJZu3VyoV0Eyb9PvsmpCEoDjWParI7Tl2E6e3A5M4tyxanoMhrpgu_XbXqtvEz6n2H7ROEd14=&X-Bogus=DFSzswVYsfXANG7Hto6K7vB9Pizp'
data3 = requests.get(url3, headers=headers).text
pat3 = re.compile('"url_list":\["http://v3-web.douyinvod.com/(.*?)\\\\')
target3 = pat3.search(data3)
path3 = 'http://v3-web.douyinvod.com/' + target3.group(1)
my_video3 = requests.get(path3, headers=headers).content
with open('知识区第一个视频.mp4', 'wb') as f:
    f.write(my_video3)
'''