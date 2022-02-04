# -*- coding: utf-8 -*-
from uuid import UUID
from .models import *


def validate_list_uuid4(uuid_list):
    new_uuid_list = []
    for uuid_string in uuid_list:
        try:
            val = UUID(uuid_string, version=4)
        except Exception as err:
            print(err)
            val = False

        if val:
            new_uuid_list.append(uuid_string)

    return new_uuid_list


def validate_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except Exception as err:
        print(err)
        val = False
    return val
