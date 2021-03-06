'''
散列表：又称哈希表
定义：散列表用的是数组支持按照下标随机访问数据的特性，所以散列表其实就是数组的一种扩展，由数组演化而来。可以说，如果没有数组，就没有散列表。
应用场景：word文档里的错误单词识别，是如何做到的？
    解答：英文大概20w个常用单词，假设一个单词平均长度是10个字母，一个单词10个字节，
        10byte * 20w = 200w byte = 200w / 1024 / 1024 = 2MB
        所以就算放大10倍也只是占用20MB内存，因此可以用散列表来存储整个英文单词词典。
思考题：
    1.假设我们有 10 万条 URL 访问日志，如何按照访问次数给 URL 排序？
        答：遍历10w url 数据将url作为key，访问次数作为value，并且同时记录下来最大访问次数k。
        如果k不是很大的话可以直接使用桶排序，如果k比较大的话（如：大于10w）可以采用快排
    2.有两个字符串数组，每个数组大约有 10 万条字符串，如何快速找出两个数组中相同的字符串？
        答：将数组A生成hash_a 表，key为字符串，value为字符串在数组A里出现的次数，
            遍历数组B，if hash_a.get(B[index]):return True else return False

散列冲突：不同的 key 对应的散列值都不一样的散列函数，几乎是不可能的，即便像业界著名的MD5、SHA、CRC等哈希算法，也无法完全避免这种散列冲突。
        而且，因为数组的存储空间有限，也会加大散列冲突的概率。
        解决办法：
            1.开放寻址：线性探测【如遇冲突则遍历寻找是否有空位】
                      二次探测【如遇冲突则每次以2次方的步长遍历寻找是否有空位】
                      双重散列【如果计算得到的存储位置已经被占用，再用第二个散列函数，依次类推，直到找到空闲的存储位置。】
            2.链表法：在散列表中，每个“桶（bucket）”或者“槽（slot）”会对应一条链表，所有散列值相同的元素我们都放到相同槽位对应的链表中。

'''
