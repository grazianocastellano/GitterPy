from gitterpy.client import GitterClient
import json 
import copy
import time
def message_list_test(chatroom):
    gitter = GitterClient('16f35f7e13c4aa642c86764a4a9a39ded30cc890')
    #list = gitter.messages.get_all_messages(chat_name)
    list1 = gitter.messages.list(chatroom)
    list2 = copy.deepcopy(list1)
    list2.reverse()
    bool = True
    while(bool is True):
        time.sleep(2)
        var = list1[0]['id']
        list1 = gitter.messages.get_messages_before_id(chatroom, var)
        list1_reverse = copy.deepcopy(list1)
        list1_reverse.reverse()
        list2 = list2 + list1_reverse
        if len(list1)<50:
            bool = False
    list2.reverse()
    print(len(list2))
    outfile_name = chatroom.split('/')[1] + '.json'
    with open(outfile_name, "w") as outfile:
        json.dump(list2, outfile)
    
    
def main_method():
    #message_list_test('laravel/laravel') --exported
    #message_list_test('rails/rails') --esported
    #message_list_test('github/linguist') --esported
    message_list_test('flutter/flutter')
    # message_list_test('github/linguist')
    #message_list_test('JabRef/jabref') --exported

if __name__ == "__main__":
    main_method()
