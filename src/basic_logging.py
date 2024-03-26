import logging

# 親ロガーを取得する
parent_logger = logging.getLogger('parent')

# 子ロガーを作成する
child_logger = parent_logger.getChild('child')

# ログメッセージを出力する
parent_logger.warning('This is a message from the parent logger')
child_logger.warning('This is a message from the child logger')

# ログレベルを設定する
parent_logger.setLevel(logging.INFO)
child_logger.setLevel(logging.DEBUG)

# ログレベルに基づいてメッセージを出力する
parent_logger.debug('This message will not be displayed')
child_logger.debug('This message will be displayed')

