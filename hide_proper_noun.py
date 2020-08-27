# coding: UTF-8
import MeCab
import pprint
def hide_proper_noun(object_text):
    def mecab_list(text):
        tagger = MeCab.Tagger('-Ochasen')
        tagger.parse('')
        node = tagger.parseToNode(text)
        word_class = []
        while node:
            word = node.surface
            wclass = node.feature.split(',')
            if wclass[0] != u'BOS/EOS':
                if wclass[6] == None:
                    word_class.append((word,wclass[0],wclass[1],wclass[2],''))
                else:
                    word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[3],wclass[6]))
            node = node.next
        return word_class
    
    word_list = mecab_list(object_text)
    #pprint.pprint(word_list)

    #固有名詞をhogeに変換してつなげる。
    changed_text_list = []
    for word in word_list:
        if word[2] != '固有名詞':
            changed_text_list.append(word[0])
        else:
            changed_text_list.append('hoge')
    changed_text = ''.join(changed_text_list)
    print(changed_text)

hide_proper_noun('')
