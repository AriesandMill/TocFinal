
from transitions import Machine


class TocBot(Machine):
    def __init__(self, **machine_configs):
        self.machine = Machine(
            model = self,
            **machine_configs
        )
    
    #is going to function
    
    def is_going_to_North(self, update):
        text = update.message.text
        return text.lower() == '北部'

    def is_going_to_Mid(self, update):
        text = update.message.text
        return text.lower() == '中部'

    def is_going_to_South(self, update):
        text = update.message.text
        return text.lower() == '南部'
    
    def is_going_to_East(self,update):
        text = update.message.text
        return text.lower() == '東部'
    
    def is_going_to_Nfood(self,update):
        text = update.message.text
        return text.lower() == '美食'

    def is_going_to_Nshop(self,update):
        text = update.message.text
        return text.lower() == '購物'

    def is_going_to_Nfun(self,update):
        text = update.message.text
        return text.lower() == '娛樂'

    def is_going_to_Mfood(self,update):
        text = update.message.text
        return text.lower() == '美食'

    def is_going_to_Mshop(self,update):
        text = update.message.text
        return text.lower() == '購物'

    def is_going_to_Mfun(self,update):
        text = update.message.text
        return text.lower() == '娛樂'

    def is_going_to_Sfood(self,update):
        text = update.message.text
        return text.lower() == '美食'

    def is_going_to_Sshop(self,update):
        text = update.message.text
        return text.lower() == '購物'

    def is_going_to_Sfun(self,update):
        text = update.message.text
        return text.lower() == '娛樂'

    def is_going_to_Efood(self,update):
        text = update.message.text
        return text.lower() == '美食'

    def is_going_to_Eshop(self,update):
        text = update.message.text
        return text.lower() == '購物'

    def is_going_to_Efun(self,update):
        text = update.message.text
        return text.lower() == '娛樂'
    
    def is_going_to_first(self,update):
        text = update.message.text
        return text.lower() == '是'

    def is_going_to_final(self,update):
        text = update.message.text
        return text.lower() == '否'
    #on enter / on exit function
    
    def on_enter_first(self,update):
        update.message.reply_text("歡迎使用traveler,請問您想去哪裡旅遊?")

    def on_enter_North(self, update):
        update.message.reply_text("想在北部進行什麼活動?")
    
    def on_enter_Mid(self, update):
        update.message.reply_text("想在中部進行什麼活動?")
      
    def on_enter_South(self, update):
        update.message.reply_text("想在南部進行什麼活動?")
    
    def on_enter_East(self,update):
        update.message.reply_text("想在東部進行什麼活動?")
    
    def on_enter_Nfood(self,update):
        update.message.reply_text("我推薦北部隱藏美食的藏寶庫--大稻埕迪化老街")
        update.message.reply_photo(open("img/nfood.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Nshop(self,update):
        update.message.reply_text("我推薦北部高格調逛街首選--台北101大樓")
        update.message.reply_photo(open("img/nshop.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Nfun(self,update):
        update.message.reply_text("我推薦北部各項娛樂一條龍--美麗華百樂園")
        update.message.reply_photo(open("img/nfun.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Mfood(self,update):
        update.message.reply_text("我推薦中部美食打卡朝聖處--宮原眼科")
        update.message.reply_photo(open("img/mfood.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Mshop(self,update):
        update.message.reply_text("我推薦中部逛街文青最愛--台中勤美天地")
        update.message.reply_photo(open("img/mshop.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Mfun(self,update):
        update.message.reply_text("我推薦中部最佳玩樂地點--麗寶探索樂園")
        update.message.reply_photo(open("img/mfun.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Sfood(self,update):
        update.message.reply_text("我推薦南部傳統美食中的霸主--文章牛肉湯")
        update.message.reply_photo(open("img/sfood.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Sshop(self,update):
        update.message.reply_text("我推薦南部逛街購物不能不去--林百貨")
        update.message.reply_photo(open("img/sshop.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Sfun(self,update):
        update.message.reply_text("我推薦南部娛樂遊玩拍照打卡最佳地點--奇美博物館")
        update.message.reply_photo(open("img/sfun.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")
    
    def on_enter_Efood(self,update):
        update.message.reply_text("我推薦東部美食大快朵頤--好漁日")
        update.message.reply_photo(open("img/efood.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Eshop(self,update):
        update.message.reply_text("我推薦東部購物體驗當地風情--台東故事館")
        update.message.reply_photo(open("img/eshop.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_Efun(self,update):
        update.message.reply_text("我推薦東部遊玩走訪自然奧妙--太魯閣國家公園")
        update.message.reply_photo(open("img/efun.jpg","rb"))
        update.message.reply_text("是否要繼續查詢?")

    def on_enter_final(self,update):
        update.message.reply_text("謝謝您的使用 祝您旅途愉快")


