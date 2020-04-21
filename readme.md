# DtoLbot

DiscordのメッセージをLINEのグループに転送するやつ
 
# Requirement
 
* heroku
 
* python 3.8.2
* discord.py
* line-bot-sdk 1.16.0
 
# Installation

* DiscordとLINEのBotを作成する
* dtolapp.pyのDISCORD_CHANNEL_IDとLINE_CHANNEL_IDを書き換える
* herokuにdeployする
* herokuの環境変数を登録する
    LINE_CHANNEL_ACCESS_TOKEN
    DISCORD_TOKEN
 
# Usage
 
Discordで'@line'を含めたメッセージを送信すると，そのメッセージが任意のLINEグループに転送されます（LINE側のbotはそのグループに参加している必要があります）．
 
# Note
 
参考文献
* https://qiita.com/suigin/items/0deb9451f45e351acf92
* https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f
* https://github.com/yuzuafro/raspi_line_beacon/blob/master/docs/pushmessage.md