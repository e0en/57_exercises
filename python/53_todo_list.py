#!/usr/bin/env python
from redis import StrictRedis


LIST_KEY = '53_todo_list'


def get_msg_list(r):
    items = r.lrange(LIST_KEY, 0, -1)
    result = []
    for i, it in enumerate(items):
        result += [f'{i + 1}. {it.decode("utf-8")}']
    return result

def write_msg(r, msg):
    todo_item = msg.strip()
    if todo_item:
        try:
            r.rpush(LIST_KEY, todo_item.encode('utf-8'))
            return True
        except Exception:
            return False

def delete_msg(r, msg_id):
    del_flag = '__DELETED__'
    try:
        msg = r.lrange(LIST_KEY, msg_id - 1, msg_id - 1)[0]
        r.lset(LIST_KEY, msg_id - 1, del_flag)
        r.lrem(LIST_KEY, 1, del_flag)
        return msg.decode('utf-8')
    except Exception:
        return False


if __name__ == '__main__':
    r = StrictRedis('127.0.0.1')

    while True:
        todos = get_msg_list(r)
        print('')
        if todos:
            print('\n'.join(todos))
        else:
            print('Yay! Nothing to do.')
        print('')
        cmd = input('add/remove: ')
        if cmd.lower() == 'add':
            msg = input('New todo: ')
            is_success = write_msg(r, msg)
            if not is_success:
                print('Failed to save your todo :(')
        elif cmd.lower() == 'remove':
            msg_id = int(input('Index of item to remove: '))
            deleted_msg = delete_msg(r, msg_id)
            if deleted_msg:
                print(f'Marked "{deleted_msg}" as done.')
            else:
                print('Failed to remove your todo :(')
        else:
            print('Bye!')
            break
