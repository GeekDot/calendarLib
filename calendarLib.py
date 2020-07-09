#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class CalendarLib(object):

    def __init__(self):

        # 天干映射表
        self.tg = {1: '甲', 2: '乙', 3: '丙', 4: '丁', 5: '戊', 6: '己', 7: '庚', 8: '辛', 9: '壬', 10: '癸'}
        # 地支映射表
        self.dz = {1: '寅', 2: '卯', 3: '辰', 4: '巳', 5: '午', 6: '未', 7: '申', 8: '酉', 9: '戌', 10: '亥', 11: '子', 12: '丑'}
        # 生肖映射表
        self.zd = {1: '鼠', 2: '牛', 3: '虎', 4: '兔', 5: '龙', 6: '蛇', 7: '马', 8: '羊', 9: '猴', 10: '鸡', 11: '狗',  0: '猪'}

    def _tg_dz(self, year):

        # 如果是公元前需要减一年，因为是负数，所以加一
        if year < 0:
            year = year + 1

        # 天干算法 ==> 年份个位 - 3，个位小于等于 3 借 10
        day = (year % 10) - 3
        if day <= 0:
            day = 10 + day

        # 地支算法 ==> 年份 + 7 和 12 取余，余数为 0，则等于 12
        ear = (year + 7) % 12
        if ear == 0:
            ear = 12

        return self.tg[day] + self.dz[ear]

    def _zodiac(self, year):

        # 如果是公元前需要减一年，因为是负数，所以加一
        if year < 0:
            year = year + 1

        # 年份数 + 9 和 12 取余
        zod = (year + 9) % 12

        return self.zd[zod]

    def get(self, year):
        if year != 0:
            return self._tg_dz(year) + ' ' + self._zodiac(year)


cl = CalendarLib()
