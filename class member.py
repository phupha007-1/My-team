# ============================================
# PART 1 : IMPORT LIBRARIES
# ============================================

import random
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta


# ใช้ seed เดิมทุกครั้งที่รัน
# เพื่อให้ข้อมูลสุ่มสามารถทำซ้ำได้
random.seed(7)


print("Import libraries สำเร็จ")

# ============================================
# PART 2 : CLASS MEMBER
# ============================================

class Member:

    def __init__(self, member_id, name, is_vip=False):

        self.member_id = member_id
        self.name = name
        self.is_vip = is_vip


    def get_member_info(self):

        return {
            "member_id": self.member_id,
            "name": self.name,
            "is_vip": self.is_vip
        }


    def __str__(self):

        member_type = "VIP" if self.is_vip else "General"

        return (
            f"Member ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Type: {member_type}"
        )


print("Class Member พร้อมใช้งาน")