from enum import Enum


class ItemStatusEnum(Enum):
    CANCEL = 'cancel'
    ORDER = 'order'
    QUOTE = 'quote'
    RECEIVE = 'received'
    REFUND = 'refund'
    TRANSPORT = 'transport'
