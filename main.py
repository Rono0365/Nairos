import time
import os
import json
import hashlib
BlockChain_dir = 'naipayBlockcrypto/'
#naipayBlockcrypto~nairos
#Rono was here
def get_hash(prev_block):
    with open(BlockChain_dir+prev_block,'a') as f:
        with open(BlockChain_dir+prev_block,'rb') as f:
            content = f.read()
        return hashlib.md5(content).hexdigest()
def check_integrity():
    files = sorted(os.listdir(BlockChain_dir),key=lambda  x:int(x))
    #print(files)
    for file in files[1:]:
        with open(BlockChain_dir + file)as f:
            block = json.load(f)
        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')
        #print()
        actual_hash = get_hash(prev_filename)
        if prev_hash == actual_hash:
            res = 'Fine'
        else:
            res = 'was changed'
        print(f'Block {prev_filename}:{res}')    
        #rono was here
   
def add_block(receiver,sender,amount):
    block_count = len(os.listdir(BlockChain_dir))
    prev_block = str(block_count)
    data={
        "receiver":receiver,
        "sender":sender,
        "amount":amount,
        "prev_block":{
            "hash":get_hash(prev_block),
            "filename":prev_block
            }

        }
    current_block = BlockChain_dir +str(len(os.listdir(BlockChain_dir))+1)
    with open(current_block,'a') as f:
    
        json.dump(data,f,indent=4,ensure_ascii=False)
        f.write('\n')

    #print(current_block)

check_integrity()
add_block('rono','idjeoi', 200)#this is how you implement adding after checking integrity for the first string add the sender and second sring the receiver alafu ya mwisho ni amount
#if __name__ == '__main__':
    
        
