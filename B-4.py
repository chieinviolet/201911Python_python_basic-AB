def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    def japan_average():
        ave = sum(d['temperature'] for d in weather_information) / len(weather_information)
        print(ave)

    japan_average()

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # join関数、リスト内包表記

    station_name = [d['station'] for d in weather_information if d['prefecture'] == '大阪府']
    print(','.join(station_name))
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    def hukuoka_tempreture():
        list_hukuoka = []
        for hukuoka_i in range(6, 8):
            list_hukuoka.append(weather_information[hukuoka_i]['temperature'])
        print(sum(list_hukuoka) / len(list_hukuoka))

    hukuoka_tempreture()




if __name__ == '__main__':
    main()
